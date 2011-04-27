'''
Created on Aug 12, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import login_page
import support_home_page
import sumo_test_data

class TestLogin(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.timeout = vars.ConnectionParameters.page_load_timeout
        self.selenium.set_timeout(self.timeout)

    def tearDown(self):
        self.selenium.stop()


    def test_login(self):
        """tests login & logout
        """
        sel = self.selenium
        login_page_obj   = login_page.LoginPage(sel)
        support_page_obj = support_home_page.SupportHomePage(sel)
        
        user_info       = sumo_test_data.SUMOtestData().getUserInfo(0)
        uname           = user_info['username']
        pwd             = user_info['password']
        
        ''' Login '''
        
        login_page_obj.log_in(uname, pwd)              
        
        login_page_obj.go_to_login_page()
        
        ''' Logout '''
        login_page_obj.log_out()
        support_page_obj.verify_page_title(support_page_obj.title)

        
if __name__ == "__main__":
    unittest.main()