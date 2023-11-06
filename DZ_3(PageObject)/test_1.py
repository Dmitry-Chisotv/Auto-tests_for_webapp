from testpage import OperationsHelper
import logging
import yaml
import time


with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# def test_step1(browser):
#     logging.info('Test 1 Starting')
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login('test')
#     testpage.enter_pass('test')
#     testpage.click_login_button()
#     assert testpage.get_error_text() == '401', "НЕВЕРНЫЙ КОД ОШИБКИ"

# def test_step2(browser):
#     logging.info('Test 2 Starting')
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login(testdata.get('login'))
#     testpage.enter_pass(testdata.get('password'))
#     testpage.click_login_button()
#     assert 'hello' in testpage.get_enter_text().lower(), "Не обнаружено слово с первой страницы. Входа не произошло"

def test_step3_DZ(browser):
    logging.info('Test DZ3 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get('login'))
    testpage.enter_pass(testdata.get('password'))
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name('test')
    testpage.enter_email('test@test.test')
    testpage.enter_content('test_test_test')
    testpage.click_contact_us_button()
    time.sleep(5)
    testpage.alert_checker()

