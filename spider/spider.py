import requests
from requests.exceptions import RequestException
import json
import pymongo
from pymongo import MongoClient
# import sys


# REQUEST_PAGES = sys.maxsize
REQUEST_PAGES = 10
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Host': 'baobab.kaiyanapp.com'
    # 'Pragma': 'no-cache'
    # 'Upgrade-Insecure-Requests': '1',
}

MONGO_DATABASE = 'eyepetizer'
MONGO_COLLECTION = 'food'
DB_CLIENT = None
DB_COLLECTION = None

def setup_database():
    global DB_CLIENT, DB_COLLECTION
    DB_CLIENT = MongoClient ()
    DB_COLLECTION = MongoClient ()[MONGO_DATABASE][MONGO_COLLECTION]
    DB_COLLECTION.create_index ([('id', pymongo.ASCENDING)], unique=True)

def shutdown_database():
    if (DB_CLIENT):
        DB_CLIENT.close ()

def request_data(url):
    try:
        resp = requests.get(url, HEADERS)
        if resp.status_code == 200:
            return  resp.text
        return None
    except RequestException:
        return None

def parse_data(data):
    if isinstance(data, str):
        jsonData = json.loads(data)
        for item in jsonData['itemList']:
            id = item['data']['id']
            print('{ id: %d }' % (id))

            exist_record = (DB_COLLECTION.find_one({ 'id': id }))
            if exist_record == None:
                DB_COLLECTION.insert_one({'id': id, 'data': item['data']})
            else:
                return None
        try:
            next_page(jsonData['nextPageUrl'])
        except KeyError:
            pass

def next_page(url):
    global REQUEST_PAGES
    REQUEST_PAGES = REQUEST_PAGES - 1
    if REQUEST_PAGES > 0:
        parse_data(request_data(url))

def main():
    setup_database()
    url = 'https://baobab.kaiyanapp.com/api/v4/categories/videoList?id=4&strategy=mostPopular'
    parse_data(request_data(url))
    shutdown_database()

if __name__ == '__main__':
    main()
