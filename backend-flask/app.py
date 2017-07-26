from flask import Flask, make_response, request
from pymongo import MongoClient
from bson import ObjectId
import json
import functools
import datetime

app = Flask(__name__)
db_client = None
db_collection = None

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

@app.route('/', methods=['GET'])
@allow_cross_domain
def index():
    page_size = request.args.get('pageSize')
    last_oid = request.args.get('lastOId')
    respJson = {'respCode': 1000,
                'respMsg': 'succ',
                'respData': fetch_index_data(page_size, last_oid) }
    jsonString = json.dumps(respJson)
    return jsonString

def fetch_index_data(page_size, last_oid):
    page_size = int(page_size) if page_size != None else 10
    result = db_collection.find().limit(page_size) if last_oid == None \
        else db_collection.find({'_id': {"$gt": ObjectId(last_oid)}}).limit(page_size)
    def filterOId(item):
        item['oid'] = str(item['_id'])
        del item['_id']
        return item
    return list(map(filterOId, result))

def get_db():
    global db_client, db_collection
    if not db_client:
        db_client = MongoClient()
        db_collection = db_client.get_database('eyepetizer').get_collection('food')

@app.teardown_appcontext
def close_db(error):
    if db_client:
        db_client.close()

if __name__ == '__main__':
    get_db()
    app.run(host='0.0.0.0',
            port=5000,
            debug=False,
            threaded=True)
