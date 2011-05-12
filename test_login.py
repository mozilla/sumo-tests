'''
Created on Aug 12, 2010

@author: mozilla
'''
from selenium import selenium
import unittest
import login_page
import sumo_test_data
import vars
import re
import support_home_page

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()
        
    def test_login(self):
        """ tests login & logout """
        sel = self.selenium
        login_page_obj   = login_page.LoginPage(sel)
        
        user_adm = 1
        user_info       = sumo_test_data.SUMOtestData().getUserInfo(user_adm)
        uname           = user_info['username']
        pwd             = user_info['password']
        
        ''' Login '''
        login_page_obj.log_in(uname, pwd)
        
        ''' Logout '''
        login_page_obj.log_out()

        
if __name__ == "__main__":
    unittest.main()