from testpage import OperationsHelper
import logging


def test_step1(browser):
    logging.info('Test Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    print('*_*' * 50)
    print(testpage.get_error_text())
    print('*_*' * 50)
    assert testpage.get_error_text() == '401', "НЕВЕРНЫЙ КОД ОШИБКИ"

