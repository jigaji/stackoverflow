import requests
import datetime
from datetime import date
from pprint import pprint
todate = date.today()
fromdate = todate - datetime.timedelta(days=2)

def get_python_request():
    url = "http://api.stackexchange.com/2.3/questions"
    params = {'fromdate': fromdate,
              'todate': todate,
              'tagged': 'python',
              'site':'stackoverflow'}
    response = requests.get(url, params=params)
    return response.json()


pprint(get_python_request())