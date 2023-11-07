from testpage import OperationsHelper, check_text
import logging
import yaml
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# def test_step1(browser):
#     logging.info('Test 1 Starting')
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login('test')
#     testpage.enter_pass('test')
#     testpage.click_login_button()
#     assert testpage.get_error_text() == '401', "НЕВЕРНЫЙ КОД ОШИБКИ"
#
# def test_step2(browser):
#     logging.info('Test 2 Starting')
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     time.sleep(5)
#     testpage.enter_login(testdata.get('login'))
#     testpage.enter_pass(testdata.get('password'))
#     testpage.click_login_button()
#     assert 'hello' in testpage.get_enter_text().lower(), "Не обнаружено слово с первой страницы. Входа не произошло"
#
# def test_step3(browser):
#     logging.info('Test DZ3 Starting')
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login(testdata.get('login'))
#     testpage.enter_pass(testdata.get('password'))
#     testpage.click_login_button()
#     testpage.click_contact_button()
#     testpage.enter_name('test')
#     testpage.enter_email('test@test.test')
#     testpage.enter_content('test_test_test')
#     testpage.click_contact_us_button()
#
# def test_step4(browser):
#     logging.info('Test 4 Starting - Create and Check new post')
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login(testdata.get('login'))
#     testpage.enter_pass(testdata.get('password'))
#     testpage.click_login_button()
#     testpage.click_new_post_button()
#     testpage.new_post_enter_title(testdata.get('new_post_title'))
#     testpage.new_post_enter_description(testdata.get('new_post_description'))
#     testpage.click_save_new_post_button()
#     time.sleep(5)
#     assert testpage.get_new_post_checker() == 'wow', "Не обнаружено слово с первой страницы. Входа не произошло"


def test_step5():
    logging.info('Test 5 Starting - Check the text')
    assert "молоко" in check_text('малако')

