import requests

def new_post(title, description, content):
    URL = "https://test-stand.gb.ru/api/posts"   #  к сожалению токен не принимается, поэтому о содержимом поста могу догадываться
    data = {
        "format": "json",
        "title": f"{title}",
        "description": f"{description}",
        "content": f"{content}",
    }

    create_post = requests.post(url=URL, data=data)
    return create_post


