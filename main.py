from config import KEY_LIST, TARGET_HTML_ID, PATH_TO_SQL, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, \
    POSTGRES_HOST, \
    POSTGRES_PORT, ELEMENTS_AMOUNT, DEFAULT_HTML_ID, PATTERN_URL
from loading_content.content_downloader import ContentDownloaderSamokat
from saving_content.db_saver import DBSaverSamokat
from utils import format_product_dict
import random

if __name__ == '__main__':

    downloader = ContentDownloaderSamokat()
    downloader.id_for_checking = DEFAULT_HTML_ID

    db_saver = DBSaverSamokat(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    db_saver.execute_sql_file(PATH_TO_SQL)

    user_command = 'start'
    pattern_url = PATTERN_URL

    while True:
        user_command = input(
            'Пожалуйста, введите url с сайта samokat.ru для загрузки информации о товарах и нажмите enter.\n'
            'Желательно, чтобы это была главная страница или адрес одной из категорий продуктов.\n'
            'Если хотите прекратить работу программы, введите "exit".\n'
            '>>> '
        )

        if user_command.lower().strip() == 'exit':
            print('Спасибо, возвращайтесь!')
            break

        if not pattern_url.match(user_command):
            print(
                'Скорее всего, не получится выполнить запрос для данного адреса.\n'
                'Пожалуйста, попробуйте другой url.\n'
            )
            continue

        downloader.url = user_command.strip()

        try:
            print('Загрузка данных...')

            my_data = downloader.get_product_dict(TARGET_HTML_ID, KEY_LIST)

            formatted_data = [format_product_dict(element) for element in my_data.values()]

            if ELEMENTS_AMOUNT <= len(formatted_data):
                product_list = random.sample(formatted_data, ELEMENTS_AMOUNT)
            else:
                product_list = formatted_data

            db_saver.save_products(product_list)
            print('Данные успешно сохранены в базу данных.\n')

        except Exception as e:
            print(f'Произошла ошибка: {e}, попробуйте ещё раз.\n')
            continue
