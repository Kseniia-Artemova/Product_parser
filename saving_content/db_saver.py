from abc import ABC, abstractmethod
import psycopg2


class DBSaver(ABC):
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.host = host
        self.conn = None
        self.cursor = None

    def create_connection(self):
        self.conn = psycopg2.connect(dbname=self.dbname,
                                     user=self.user,
                                     password=self.password,
                                     host=self.host,
                                     port=self.port)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

    @abstractmethod
    def execute_sql_file(self, file_path):
        pass

    @abstractmethod
    def save_products(self, product_dict):
        pass


class DBSaverSamokat(DBSaver):
    def __init__(self, dbname, user, password, host, port):
        super().__init__(dbname, user, password, host, port)

    def execute_sql_file(self, file_path):
        try:
            self.create_connection()

            with open(file_path, 'r') as file:
                sql_script = file.read()
            self.cursor.execute(sql_script)
            self.conn.commit()

        finally:
            self.close_connection()

    def save_products(self, product_list):
        try:
            self.create_connection()

            for product in product_list:
                keys = ', '.join(product.keys())
                placeholders = ', '.join(['%s'] * len(product))
                update_statement = ', '.join([f"{key} = EXCLUDED.{key}" for key in product.keys()])

                self.cursor.execute(f"""
                    INSERT INTO products ({keys})
                    VALUES ({placeholders})
                    ON CONFLICT (id) DO UPDATE SET
                    {update_statement};
                """, tuple(product.values()))
                self.conn.commit()

        finally:
            self.close_connection()
