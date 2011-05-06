#!/usr/bin/env python
'''
Created on May 6, 2011

@author: mozilla
'''

from selenium import selenium
import vars
import unittest
import datetime

import questions_page
import login_page
import sumo_test_data

class TestAAQ(unittest.TestCase):
    
    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.timeout = vars.ConnectionParameters.page_load_timeout
        self.selenium.set_timeout(self.timeout)

    def tearDown(self):
        self.selenium.stop()

                
    def test_that_posting_question_works(self):
        """Posts a question to /questions"""
        sel                 = self.selenium
        login_po      = login_page.LoginPage(sel)
        questions_po = questions_page.QuestionsPage(sel)
        timestamp = sel.get_eval("new Date().getTime()")
        q_to_ask = "automation test question %s" %(datetime.date.today())
        q_details = "This is a test. " + timestamp


        user_info       = sumo_test_data.SUMOtestData().getUserInfo(0)
        uname           = user_info['username']
        pwd             = user_info['password']
        
        ''' login '''
        login_po.log_in(uname, pwd)
        
        """ go to the /questions/new page and post a question
        """
        questions_po.go_to_ask_new_questions_page()
        questions_po.click_firefox_product_link()
        questions_po.click_category_problem_link()
        questions_po.type_question(q_to_ask)
        questions_po.click_provide_details_button()
        questions_po.fill_up_questions_form(q_details)
        
        self.failUnless(sel.is_text_present(q_to_ask))
        self.failUnless(sel.is_text_present(q_details))
        
if __name__ == "__main__":
    unittest.main()                                               