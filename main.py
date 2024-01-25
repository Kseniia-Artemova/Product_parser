from config import URL, KEY_LIST, HTML_ID, PATH_TO_SQL, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, \
    POSTGRES_PORT, ELEMENTS_AMOUNT
from loading_content.content_downloader import ContentDownloaderSamokat
from saving_content.db_saver import DBSaverSamokat
from utils import format_product_dict
import random

downloader = ContentDownloaderSamokat()
downloader.url = URL
my_data = downloader.get_product_dict(HTML_ID, KEY_LIST)

formatted_data = [format_product_dict(element) for element in my_data.values()]
product_list = random.sample(formatted_data, ELEMENTS_AMOUNT)

db_saver = DBSaverSamokat(
    dbname=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT
)

db_saver.execute_sql_file(PATH_TO_SQL)
db_saver.save_products(product_list)




