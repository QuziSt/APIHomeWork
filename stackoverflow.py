import requests
from pprint import pprint
from datetime import datetime,timedelta

url = 'https://api.stackexchange.com/2.3/search/'
period = 2
now = datetime.now()
to_date = int(datetime.timestamp(now))
from_date = int(datetime.timestamp(now - timedelta(days=period)))
respond = requests.get(url, params={'fromdate': from_date, 'todate': to_date, 'tagged': 'Python', 'site': 'stackoverflow'})
pprint(respond.json())
