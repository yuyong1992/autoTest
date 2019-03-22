# coding:utf-8

import HTMLTestReportCN
import unittest
import time
# import os
# from autoRB.cases.test_login import Login
from autoRB.cases.test_login import LoginErr, LoginSuccess, LinkClick

# 以下是几种将测试用例添加到测试套件中的方法

# 通过测试类查找测试用例
suit = unittest.TestSuite()
# suit.addTest(unittest.makeSuite(LoginSuccess))
# suit.addTest(unittest.makeSuite(LoginErr))
suit.addTest(unittest.makeSuite(LinkClick))

# 通过测试类查找测试用例
# suit = unittest.TestLoader().loadTestsFromTestCase(LoginErrPhone)

# 通过测试用例文件*py查找
# path_case = os.path.join(os.getcwd(), 'cases')
# suit = unittest.TestLoader().discover(path_case, pattern="test*.py", top_level_dir=None)

if __name__ == '__main__':
    report_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_dir = r'./report/report' + report_time + r'.html'
    file = open(report_dir, 'wb')

    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=file,
        title=r'登录测试',
        description=r'不同角色登录测试',
        tester='Yuyong'
    )
    runner.run(suit)
