from flask import Flask
from flask import make_response
from pymongo import MongoClient
import json
import functools

app = Flask(__name__)
data_list = []

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

@app.route('/')
@allow_cross_domain
def index():
    respJson = {'respCode': 1000,
                'respMsg': 'succ',
                'respData': data_list }
    return json.dumps(respJson)

def fetch_data():
    db_client = MongoClient()
    db_collection = db_client.get_database('test').get_collection('eyepetizer-food')
    for item in db_collection.find({}, {'_id': False}):
        data_list.append(item)
    db_client.close()

if __name__ == '__main__':
    fetch_data()
    app.run(host='0.0.0.0')
