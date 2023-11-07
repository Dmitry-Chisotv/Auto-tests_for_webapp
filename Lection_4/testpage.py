from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
from zeep import Client, Settings, client


class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')

        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def clicl_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    # ENTER TEXT - методы ввода текста

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='password form')

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NAME_FIELD'], word, description='name to contact form')

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_EMAIL_FIELD'], word, description='email to contact form')

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'], word, description='content to contact form')

    def new_post_enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE_NEW_POST_FIELD'], word, description='Enter title to new post')

    def new_post_enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESCRIPTION_NEW_POST_FIELD'], word, description='Enter description to new post')

# CLICK -  методы нажатия кнопок
    def click_login_button(self):
        self.clicl_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login button')

    def click_contact_button(self):
        self.clicl_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description='contact button')

    def click_contact_us_button(self):
        self.clicl_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description='contact us button')

    def click_new_post_button(self):
        self.clicl_button(TestSearchLocators.ids['LOCATOR_NEW_POST_BTN'], description='New post button')

    def click_save_new_post_button(self):
        self.clicl_button(TestSearchLocators.ids['LOCATOR_SAVE_NEW_POST_BTN'], description='Save new post button')

# GET TEXT -  методы получения текста

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='get error text')

    def get_enter_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_TEXT_FIELD'], description='get enter text')

    def get_contact_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_CONTACT_CHECKER_FIELD'], description='get contact text')

    def get_new_post_checker(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_NEW_POST_CHECKER'], description='get New post text for check')

    def get_alert_checker(self):
        logging.info('Check Alert')
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f'We find text {text} in enter-page ALERT')
        assert """Form successfully submitted""" in text, "Текст Алерта не обнаружен"


def check_text(word):
    with open("testdata.yaml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    settings = Settings(strict=False)
    client = Client(wsdl=data["url"], settings=settings)
    return client.service.checkText(word)[0]['s']
