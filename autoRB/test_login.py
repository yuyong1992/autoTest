# coding:utf-8

import unittest
from autoRB.pages.login_page import LoginPage
from autoRB.framework.browser_engine import BrowserEngine
from autoRB.framework.logger import Logger

logger = Logger(logger='LoginPage').getlog()


class Login(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_1_login_channel(self):
        """渠道商登录成功"""
        username = '18811133441'
        pwd = '1234qwer'
        loginpage = LoginPage(self.driver)
        loginpage.wait(2)
        loginpage.type_username(username)
        loginpage.type_pwd(pwd)
        loginpage.click_but()
        try:
            self.assertIn('RBSS', loginpage.get_page_title())
            print('%s Login Test Pass!' % username)
            logger.info('%s Login Test Pass!' % username)
        except AssertionError as e:
            logger.error('%s 登录失败！ err: %s' % (username, e))
            print('Test Fail ! err: %s' % e)
            raise AssertionError

    def test_2_login_S1(self):
        """S1登录成功"""
        username = '18811133442'
        pwd = '1234qwer'
        loginpage = LoginPage(self.driver)
        loginpage.wait(2)
        loginpage.type_username(username)
        loginpage.type_pwd(pwd)
        loginpage.click_but()
        try:
            self.assertIn('RBSS', loginpage.get_page_title())
            print('%s Login Test Pass!' % username)
            logger.info('%s Login Test Pass!' % username)
        except AssertionError as e:
            logger.error('%s 登录失败！ err: %s' % (username, e))
            print('Test Fail ! err: %s' % e)
            raise AssertionError


if __name__ == '__main__':
    unittest.main()
