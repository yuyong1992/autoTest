# coding:utf-8

import unittest
from autoRB.pages.dashboard_page import DashBoardPage
from autoRB.framework.browser_engine import BrowserEngine


class LinkClick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine()
