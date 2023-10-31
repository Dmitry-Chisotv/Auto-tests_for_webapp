from login import get_post
from new_post import new_post
import pytest

def test_step1(login):
    res = get_post(login)
    res_list = res.get("data")
    res_id_list = [item['id'] for item in res_list]
    assert 1234 in res_id_list, 'тест не пройден'

def test_step2(new_post):
    result_for_check = new_post.json()['description']
    assert "description_1" in result_for_check, 'Пост не создан'

if __name__ == "__main__":
    pytest.main(["-vv"])