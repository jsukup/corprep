import os
from newscatcherapi import NewsCatcherApiClient
from dotenv import load_dotenv
import json

load_dotenv()
newscatcher_api = os.getenv('NEWSCATCHER_API')

newscatcherapi = NewsCatcherApiClient(x_api_key=newscatcher_api)

mst_articles = newscatcherapi.get_search_all_articles(q="Morgan Stanley",
                                                      lang='en',
                                                      countries='US',
                                                      page_size=100,
                                                      max_page=5,
                                                      by='day')

file_path = 'morgan_stanley.json'
with open(file_path, 'w') as f:
    json.dump(mst_articles, f)

