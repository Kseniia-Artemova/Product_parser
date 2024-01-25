import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# URL = 'https://web.samokat.ru'
URL = 'https://samokat.ru/category/moloko-yajca-i-syr-jogurty-i-deserty'
HEADER = os.getenv('HEADER')
HTML_ID = '__NEXT_DATA__'
KEY_LIST = ['props', 'pageProps', 'initialState', 'products', 'entities']
ELEMENTS_AMOUNT = 20

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
PATH_TO_SQL = Path(__file__).parent / 'saving_content' / 'create_product_table_samokat.sql'