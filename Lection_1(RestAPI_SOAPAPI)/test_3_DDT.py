import requests

S = requests.Session()

def get_sites(lat, long, radius, limit=100):
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": f"{limit}",
        "gsradius": f"{radius}",
        "action": "query"
    }

    r = S.get(url=URL, params=PARAMS)
    pages = r.json()['query']['geosearch']
    sites = [i["title"] for i in pages]
    return sites

# print(get_sites("37.7891838", "-122.4033522", 100))

def test_step1(text1, coord1):
    assert text1 in get_sites(coord1[0], coord1[1], 100), "NOT FOUND"

# def test_step1():
#     assert "One MOTgomery Tower" in get_sites("37.7891838", "-122.4033522", 100), "NOT FOUND"

test_step1()