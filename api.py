import json

import requests

import conf

BASE_URL = conf.API_URL


def get_cat() -> str:
    resp = requests.get(BASE_URL)

    if resp.status_code == 404:
        raise FileNotFoundError(f"url={BASE_URL},status_code={resp.status_code}")
    if resp.status_code != 200:
        raise Exception(f"url={BASE_URL},status_code={resp.status_code}")

    data: dict = json.loads(resp.text)[0]   # json.loads -> [{response1}] it's list with dict inside

    cat_url = data['url']

    return cat_url


