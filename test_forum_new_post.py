'''
Created on Jul 20, 2010

@author: mozilla
'''
from selenium import selenium
import vars
import time
import unittest

import forums_page
import login_page
import sumo_test_data

class ForumPagination(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.timeout = vars.ConnectionParameters.page_load_timeout
        self.selenium.set_timeout(self.timeout)


    def tearDown(self):
        self.selenium.stop()


    def test_forum_new_post(self):
        """Post a new thread in the KB articles forums"""
        sel = self.selenium
        login_page_obj   = login_page.LoginPage(sel)
        forums_page_obj  = forums_page.ForumsPage(sel)
        
        user_info       = sumo_test_data.SUMOtestData().getUserInfo(0)
        uname           = user_info['username']
        pwd             = user_info['password']
        timestamp       = sel.get_eval("new Date().getTime()")
        thread_title    = "Litmus 7829 test" + timestamp
        thread_text     = "Litmus QA 7829 Testcase Test Msg"
        
        ''' Login '''
        login_page_obj.log_in(uname, pwd)         
        
        
        ''' Post a new thread '''
        forums_page_obj.open(forums_page_obj.kb_articles_forum_url)
        forums_page_obj.post_new_thread_first_cat(thread_title, thread_text)

        time.sleep(5)
        self.failUnless(sel.is_text_present(thread_text))
        # Verify post title
        forums_page_obj.open(forums_page_obj.kb_articles_forum_url)
        self.failUnless(sel.is_text_present(thread_title))
        
        ''' Logout '''
        forums_page_obj.log_out()
        
if __name__ == "__main__":
    unittest.main()