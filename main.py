from pprint import pprint

from config import URL, KEY_LIST, HTML_ID
from loading_content.content_downloader import ContentDownloaderSamokat

downloader = ContentDownloaderSamokat()
downloader.url = URL
my_data = downloader.get_product_dict(HTML_ID, KEY_LIST)

pprint(my_data)

