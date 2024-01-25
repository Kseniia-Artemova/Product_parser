import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# URL = 'https://web.samokat.ru'
URL = 'https://samokat.ru/category/hleb-i-vypechka-hlebcy-suhari-i-sushki'
HEADER = os.getenv('HEADER')
HTML_ID = '__NEXT_DATA__'
KEY_LIST = ['props', 'pageProps', 'initialState', 'products', 'entities']