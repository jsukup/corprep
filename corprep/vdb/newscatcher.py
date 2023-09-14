import os
from newscatcherapi import NewsCatcherApiClient
from dotenv import load_dotenv
import json

load_dotenv()
newscatcher_api = os.getenv('NEWSCATCHER_API')

newscatcherapi = NewsCatcherApiClient(x_api_key=newscatcher_api)

banks = ['Bank of America','Citigroup','Goldman Sachs','JPMorgan Chase','Wells Fargo']
retailers = ['Walmart','Amazon','Target','Costco','CVS','Walgreens']
auto = ['General Motors','BMW','Honda','Ford','Volkswagen','Mercedes-Benz','Toyota','Tesla','Hyundai']

def newscatcher_scrape(queries: list[str]):
    for query in queries:
        mst_articles = newscatcherapi.get_search_all_pages(q=query,
                                                   lang='en',
                                                   countries='US',
                                                   page_size=1,
                                                   max_page=1)
        file_path = f'C:/mldev/corprep/data/{query}.json'
        with open(file_path, 'w') as f:
            json.dump(mst_articles, f)
            
newscatcher_scrape(banks)