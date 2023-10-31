import requests
import yaml
import pytest

with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    responce = requests.post(url=data.get('url_login'),
                             data={"username": data.get('username'),
                                   "password": data.get("password")})

    if responce.status_code == 200:
        return responce.json()['token']