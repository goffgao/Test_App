#test_Pytest.py文件1
#coding=utf-8
# import os
# import sys
# sys.path.append(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
#试下
import pytest,allure

class Test_Abc_001():
        @allure.step(title='测试标题')
        def test_one(self):
            allure.attach('断言')
            assert 0

if __name__=="__main__":
    pytest.main('-s --alluredir allure-report')

