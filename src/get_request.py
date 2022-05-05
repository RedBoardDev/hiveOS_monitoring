import requests
from dotenv import dotenv_values

secrets = dotenv_values(".env")
token_discord = secrets["DISCORD_TOKEN"]
HIVETOKEN = secrets["HIVE_TOKEN"]
HIVEFARM = secrets["HIVEFARM"]
HIVEWORKER = secrets["HIVEWORKER"]
url = 'https://api2.hiveos.farm/api/v2/farms/776169/workers/1669282/metrics'

def request_json(url):
    req = requests.get(url, headers={'Authorization': 'Bearer ' + HIVETOKEN}, params="period=1d").json()
    return (req)

def get_workers_metrics():
    return (request_json(url)['data'][-1])