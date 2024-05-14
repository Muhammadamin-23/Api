import requests
import json
from pprint import pprint as pp

url = "https://api-lrb4.onrender.com/api/v1/posts/"

payload = ''
headers = {
    'Authorization': 'Basic YWRtaW46MTIzNA=='
}


def get_posts():
    response = requests.request("GET", url, headers=headers, data=payload)
    my_json = json.loads(response.text)
    return my_json
    pp(my_json)

