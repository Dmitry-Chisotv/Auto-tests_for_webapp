from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:

    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_TEXT_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_CHECKER_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_NAME_FIELD =  (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click logging button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_enter_text(self):
        enter_field = self.find_element(TestSearchLocators.LOCATOR_TEXT_FIELD, time=3)
        text = enter_field.text
        logging.info(f'We find text {text} in enter-page field {TestSearchLocators.LOCATOR_TEXT_FIELD[1]}')
        return text

    def click_contact_button(self):
        logging.info('Click contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def get_contact_text(self):
        enter_contact_checker = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CHECKER_FIELD, time=3)
        text = enter_contact_checker.text
        logging.info(f'We find text {text} in enter-page field {TestSearchLocators.LOCATOR_CONTACT_CHECKER_FIELD[1]}')
        return text

    def enter_name(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)
        logging.info('Check Assert for name field in Contact Us')
        assert name_field.get_attribute('value') == 'test'


    def enter_email(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)
        logging.info('Check Assert for email field in Contact Us')
        assert email_field.get_attribute('value') == 'test@test.test'

    def enter_content(self, word):
        logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)
        logging.info('Check Assert for contact field in Contact Us')
        assert content_field.get_attribute('value') == 'test_test_test'

    def click_contact_us_button(self):
        logging.info('Click Contact Us button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def alert_checker(self):
        logging.info('Check Alert')
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f'We find text {text} in enter-page ALERT')
        assert """Form successfully submitted""" in text, "Текст Алерта не обнаружен"
