import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()




### shift + tab - перенос текста влево

# with open('testdata.yaml') as f:
#     testdata = yaml.safe_load(f)
#
# @pytest.fixture()
# def selector_login():
#     return """//*[@id="login"]/div[1]/label/input"""
#
#
# @pytest.fixture()
# def selector_password():
#     return """//*[@id="login"]/div[2]/label/input"""
#
#
# @pytest.fixture()
# def selector_button():
#     return 'button'
#
#
# @pytest.fixture()
# def selector_error():
#     return """//*[@id="app"]/main/div/div/div[2]/h2"""
#
# @pytest.fixture()
# def site():
#     site_inst = Site(testdata['address'])
#     yield site_inst
#     site_inst.my_quit()
