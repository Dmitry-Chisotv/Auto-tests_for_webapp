import yaml
from module_py import Site
import pytest

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata['address'])

#def test_step1(site, selector_login, selector_password, selector_button, selector_error):
def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element('xpath', x_selector1)
    #input1 = site.find_element('xpath', selector_login)
    input1.send_keys('test')

    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element('xpath', x_selector2)
    #input2 = site.find_element('xpath', selector_password)
    input2.send_keys('test')

    btn_selector = 'button'
    btn = site.find_element('css', btn_selector)
    #btn = site.find_element('css', selector_button)
    btn.click()

    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element('xpath', x_selector3)
    #err_label = site.find_element('xpath', selector_error)
    # print(err_label.text)
    assert err_label.text == '401', "НЕВЕРНЫЙ КОД ОШИБКИ"

    input1.clear()
    input2.clear()

def test_step2():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element('xpath', x_selector1)
    #input1 = site.find_element('xpath', selector_login)
    input1.send_keys('GB2023059a00e4')

    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element('xpath', x_selector2)
    #input2 = site.find_element('xpath', selector_password)
    input2.send_keys('e8b141b383')

    btn_selector = 'button'
    btn = site.find_element('css', btn_selector)
    #btn = site.find_element('css', selector_button)
    btn.click()

    x_selector3 = """//*[@id="app"]/main/div/div/h1"""
    site_enter = site.find_element('xpath', x_selector3)
    assert site_enter.text == 'Student Page', "НЕ прошел позитивную проверку"

#test_step1()

if __name__ == '__main__':
    pytest.main(['-vv'])

