'''
Created on Oct 11, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest
import random
import time

import questions_page

class QuestionProbCount(unittest.TestCase):

    thread_loc = ''
    thread_num = str(random.randint(100, 10000))
    thread_title = 'test_thread_' + thread_num
    thread_text = 'some text'

    
    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.timeout = vars.ConnectionParameters.page_load_timeout
        self.selenium.set_timeout(self.timeout)

    def tearDown(self):
        self.selenium.stop()

                
    def test_questions_problem_count(self):
        """Checks if the 'I have this problem too' counter increments"""
        sel                 = self.selenium
        #login_page_obj      = login_page.LoginPage(sel)
        questions_page_obj  = questions_page.QuestionsPage(sel)


#        user_info       = sumo_test_data.SUMOtestData().getUserInfo(0)
#        uname           = user_info['username']
#        pwd             = user_info['password']
#        
#        ''' login '''
#        login_page_obj.log_in(uname, pwd)
        
        """ click on a question from the list of 20 questions 
            If a question does not have 'I have this problem too' 
            button then keep clicking through the list until you find one
        """
        found = False
        counter = 0
        while(not found and counter<20):
            num = random.randint(1, 20)
            questions_page_obj.go_to_forum_questions_page()
            questions_page_obj.click_any_question(num)
            if(sel.is_element_present(questions_page_obj.problem_too_button)):
                found = True
            counter = counter+1
        
        if(not found and counter==20):
            return
            
        initial_count = questions_page_obj.get_problem_count()     
        questions_page_obj.click_problem_too_button()
        time.sleep(2)
        questions_page_obj.refresh(vars.ConnectionParameters.page_load_timeout)
        post_click_count = questions_page_obj.get_problem_count()
        
        self.assertEqual(initial_count+1,post_click_count)
        
if __name__ == "__main__":
    unittest.main()                                               