import time
import yaml
from module_py import Site
import pytest

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata['address'])

def test_step1():
    # x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    # input1 = site.find_element('xpath', x_selector1)
    # input1.send_keys('olegpopov1111111')
    # x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    # input2 = site.find_element('xpath', x_selector2)
    # input2.send_keys('9164f4875d')
    # btn_selector = 'button'
    # btn = site.find_element('css', btn_selector)
    # btn.click()

    # LOCATOR_NEW_POST_BTN #add_post_button = """//*[@id="app"]/main/div/div[2]/div[1]"""
    btn_add = site.find_element('xpath', add_post_button)
    btn_add.click()

    # LOCATOR_TITLE_NEW_POST_FIELD # x_selector_title = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    input_title = site.find_element('xpath', x_selector_title)
    input_title.send_keys('wow')

    # LOCATOR_DESCRIPTION_NEW_POST_FIELD # x_selector_desciption = """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    input_descr = site.find_element('xpath', x_selector_desciption)
    input_descr.send_keys('test-test-test for DZ2____DZ2')
    # LOCATOR_SAVE_NEW_POST_BTN # x_selector_save_btn = """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
    btn_save_post = site.find_element('xpath', x_selector_save_btn)
    btn_save_post.click()

    time.sleep(5)

    # LOCATOR_NEW_POST_CHECKER # x_selector_checker_post = """//*[@id="app"]/main/div/div[1]/h1"""
    site_checker_post = site.find_element('xpath', x_selector_checker_post)
    assert site_checker_post.text == 'wow', "НЕ прошел позитивную проверку"


if __name__ == '__main__':
    pytest.main(['-vv'])