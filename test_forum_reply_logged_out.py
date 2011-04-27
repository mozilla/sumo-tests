'''
Created on Jul 21, 2010

@author: mozilla
'''
from selenium import selenium
import vars
import unittest

import forums_page

class ForumReply(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.timeout = vars.ConnectionParameters.page_load_timeout
        self.selenium.set_timeout(self.timeout)

    def tearDown(self):
        self.selenium.stop()


    def test_forum_reply_logged_out(self):
        """Tests to ensure Reply link is not available when logged-out
        """
        sel = self.selenium
        forums_page_obj  = forums_page.ForumsPage(sel)
        
                
        ''' go to forums page '''
        forums_page_obj.go_to_forums_cat_list_page()
        forums_page_obj.click(forums_page_obj.first_cat_forum_link,True)

        
        counter = 0
        unlocked_not_found = True
        while(unlocked_not_found and counter < 11):
           
            '''
            click on a thread starting with the first and
            work your way down the list until you have checked 10
            thread and none of them are unlocked
            '''
            counter = counter + 1
            if(forums_page_obj.is_element_present(forums_page_obj.locked_thread_format %(counter))):
                continue
            else:
                unlocked_not_found = False
                forums_page_obj.click((forums_page_obj.unlocked_thread_format %(counter)), True)
                self.failIf(sel.is_element_present(forums_page_obj.reply_link),
                    "Reply not disabled")
        
if __name__ == "__main__":
    unittest.main()