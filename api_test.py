import requests
from pprint import pprint as pp
import json

url = "http://127.0.0.1:8000/api/v1/posts/"
putch_url = "http://127.0.0.1:8000/api/v1/posts/3/"

payload = json.dumps({
    "title": "3 post",
    "content": "Uchinchiinchi content",
    "is_published": True
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46MTIzNA=='
}


def get_all_posts():
    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    return json_data


def patch_all_posts():
    response = requests.request("PATCH", putch_url, headers=headers, data=payload)
    json_date = json.loads(response.text)
    return json_date


def del_all_posts():
    response = requests.request("DEL", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    return json_data


if __name__ == "__main__":
    data = patch_all_posts()
    pp(data)
