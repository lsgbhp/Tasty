import config
import requests
from requests.exceptions import RequestException
import json
import time
import pymongo
from pymongo import MongoClient

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'baobab.kaiyanapp.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1'
}

db_client = MongoClient()
db_collection_popular = db_client[config.DATABASE][config.COLLECTION_POPULAR]
db_collection_recent = db_client[config.DATABASE][config.COLLECTION_RECENT]

def shutdown_database():
    if (db_client):
        db_client.close()

def request_data(url):
    try:
        resp = requests.get(url, HEADERS)
        if resp.status_code == 200:
            return  resp.text
        return None
    except RequestException:
        return None

def fetch_popular_data():
    request_times_popular = config.REQUEST_TIMES_POPULAR
    def parse_popular_data(data):
        if not(isinstance(data, str)):  return
        jsonData = json.loads(data)
        for item in jsonData['itemList']:
            id = item['data']['id']
            print ('{insert popular data, id: %d }' % (id))
            db_collection_popular.insert_one({
                'id': id,
                'data': item['data']
            })
        nonlocal request_times_popular
        request_times_popular = request_times_popular - 1
        if request_times_popular > 0:
            try:
                parse_popular_data(request_data(jsonData['nextPageUrl']))
            except KeyError:
                pass

    db_collection_popular.drop()
    db_collection_popular.create_index ('id', unique=True)
    parse_popular_data (request_data ('https://baobab.kaiyanapp.com/api/v4/categories/videoList?id=4&strategy=mostPopular'))

def fetch_rencent_data():
    request_times_recent = config.REQUEST_TIMES_RECENT
    def parse_recent_data(data):
        if not (isinstance (data, str)):  return
        jsonData = json.loads(data)
        for item in jsonData['itemList']:
            id = item['data']['id']
            exist_record = (db_collection_recent.find_one({ 'id': id }))
            if exist_record == None:
                print ('{insert recent data, id: %d }' % (id))
                db_collection_recent.insert_one({
                    'id': id,
                    'data': item['data']
                })
            else:
                return
        nonlocal request_times_recent
        request_times_recent = request_times_recent - 1
        if request_times_recent > 0:
            try:
                parse_recent_data(request_data(jsonData['nextPageUrl']))
            except KeyError:
                pass

    db_collection_recent.create_index([('id', pymongo.DESCENDING)], unique=True)
    parse_recent_data (request_data ('https://baobab.kaiyanapp.com/api/v4/categories/videoList?id=4'))

def main():
    fetch_rencent_data()
    fetch_popular_data()
    shutdown_database()

if __name__ == '__main__':
    main()
