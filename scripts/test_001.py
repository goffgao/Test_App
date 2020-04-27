#test_Pytest.py文件1
#coding=utf-8
import os
import sys
sys.path.append(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

import pytest , allure

class Test_Abc_001():
        @allure.step(title='第一个测试')
        def test_one(self,):
            allure.attach('这是一个藐视','试一下')
            assert 1

if __name__=="__main__":
    pytest.main('-s --alluredir report')

