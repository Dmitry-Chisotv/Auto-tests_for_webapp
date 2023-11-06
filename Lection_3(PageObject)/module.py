import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']

#service = Service(testdata['driver_path'])
# options = webdriver.ChromeOptions()

class Site:


    def find_element(self, mode, path):
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        elif mode == 'class':
            element = self.driver.find_element(By.CLASS_NAME, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)


