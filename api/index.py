from flask import Flask, Response, request, abort
from flask_caching import Cache
import yfinance as yf

import requests
import json
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "bd7a2cf8c82889ba963ffc6b033d42d2d9a498f3"
app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 0 # dont time out
cache = Cache(app)

#register 500 error handler
@app.errorhandler(Exception)
# handle all other exception
def all_exception_handler(error):
    res = {"error": str(error)}
    return Response(status=500, mimetype="application/json", response=json.dumps(res))

# handle 401 exception
def error_401_handler(error):
    res = {"error": "Unauthorized"}
    return Response(status=401, mimetype="application/json", response=json.dumps(res))

# handle 413 exception
def error_413_handler(error):
    res = {"error": error.description}
    return Response(status=413, mimetype="application/json", response=json.dumps(res))


# API section

@app.route('/', methods=['GET'])
@app.route('/price', methods=['GET'])
def getPrice():
    # check api key
    if 'apikey' not in request.args:
        abort(401)
    # verify api key
    if not verify(request.args.get('apikey', type=str)):
        abort(401)
    # log access key
    print(request.args.get('apikey', type=str))

    symbol = request.args.get('symbol', type=str)
    days = request.args.get('days', default=5, type=int)
        
    if not symbol:
        about(413, "No symbol provided")
        
    if days > 60:
        abort(413, "Days too large, max 60 days")
    elif days < 5:
        interval = "1m"
    elif days < 10:
        interval = "5m"
    elif days <= 30:
        interval = "15m"
    else:
        interval = "1d"
    days = str(days) + "d"

    if "," in symbol:
        symbols = symbol.split(",")
    else:
        symbols = [symbol]
    
    final_dict = dict()
    for sym in symbols:
        price = yf.Ticker(sym).history(period=days, interval=interval)
        final_dict[sym] = getPriceDict(price)

    return Response(status=200, mimetype="application/json", response=json.dumps(final_dict))


@app.route('/mylist')
def getMYStockList():
    # check api key
    if 'apikey' not in request.args:
        abort(401)
    # verify api key
    if not verify(request.args.get('apikey', type=str)):
        abort(401)
    # log access key
    print(request.args.get('apikey', type=str))
    
    if cache.get("my_stock_list") is None:
        preGetStockList()
    return Response(status=200, mimetype="application/json", response=json.dumps(cache.get("my_stock_list")))

def getPriceDict(tickerHistory):
    price_dict = tickerHistory.to_dict()
    for key in price_dict:
        price_dict[key] = {int(x.value/10**6): round(y,4) for x, y in price_dict[key].items()}
    return price_dict


# init keys
ACCESS_KEYS = os.environ["keys"].split(",")
def verify(key):
    return key in ACCESS_KEYS

# init dict to return, cache result
def preGetStockList():
    response_dict = requests.get("https://api.twelvedata.com/stocks?country=MY").json()['data']
    for stock in response_dict:
        stock['symbol'] = stock['symbol']+".MY"
    cache.add("my_stock_list", response_dict)
