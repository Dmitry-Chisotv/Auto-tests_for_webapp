import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)
def login():
    responce = requests.post(url=data.get('url_login'),
                             data={"username": data.get('username'),
                                   "password": data.get("password")})

    if responce.status_code == 200:
        return responce.json()['token']

def get_post(token):
    print(token)
    resp = requests.post(url=data.get('url_post'),
                             headers= {"X-Auth-Token": token},
                             params={ "owner": "notMe"})
    print(resp.json())
    return resp.json()


if __name__ == '__main__':
    #print(login())
    get_post(login())