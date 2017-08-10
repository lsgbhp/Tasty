from flask import Flask, make_response, request
import pymongo
from pymongo import MongoClient
from bson import ObjectId
import json
import functools
import config

app = Flask(__name__)

db_client = MongoClient()
db_collection_popular = db_client[config.DATABASE][config.COLLECTION_POPULAR]
db_collection_recent = db_client[config.DATABASE][config.COLLECTION_RECENT]

def allow_cross_domain(fun):
    @functools.wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun


@app.route('/api/index', methods=['GET'])
@allow_cross_domain
def index():
    page_size = request.args.get('pageSize')
    last_id = request.args.get('lastId')
    respJson = {
        'respCode': 1000,
        'respMsg': 'succ',
        'respData': fetch_recent_data(page_size, last_id)
    }
    jsonString = json.dumps(respJson)
    return jsonString

@app.route('/api/popular', methods=['GET'])
@allow_cross_domain
def popular():
    page_size = request.args.get('pageSize')
    last_oid = request.args.get('lastOId')
    respJson = {
        'respCode': 1000,
        'respMsg': 'succ',
        'respData': fetch_popular_data(page_size, last_oid)
    }
    jsonString = json.dumps(respJson)
    return jsonString

def fetch_recent_data(page_size, last_id):
    page_size = int(page_size) if page_size != None else 10
    result = db_collection_recent.find().sort([('id', pymongo.DESCENDING)]).limit(page_size) if last_id == None \
        else db_collection_recent.find({'id': {"$lt": int(last_id)}}).sort([('id', pymongo.DESCENDING)]).limit(page_size)
    def filterOId(item):
        item['oid'] = str(item['_id'])
        del item['_id']
        return item
    return list(map(filterOId, result))

def fetch_popular_data(page_size, last_oid):
    page_size = int(page_size) if page_size != None else 10
    result = db_collection_popular.find().limit(page_size) if last_oid == None \
        else db_collection_popular.find({'_id': {"$gt": ObjectId(last_oid)}}).limit(page_size)
    def filterOId(item):
        item['oid'] = str(item['_id'])
        del item['_id']
        return item
    return list(map(filterOId, result))

@app.teardown_appcontext
def close_db(error):
    if db_client:
        db_client.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=False,
            threaded=True)
