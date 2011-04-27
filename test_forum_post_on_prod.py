'''
Created on Feb 14, 2011

@author: mozilla
'''

from selenium import selenium
import vars
import unittest
import random
import time

import forums_page
import login_page
import sumo_test_data

class ForumPostProd(unittest.TestCase):

    thread_loc = ''
    thread_num = str(random.randint(100, 10000))
    thread_title = 'test_thread_' + thread_num
    thread_text = 'some text'

    
    def setUp(self):
        pass

    def tearDown(self):
        self.selenium.stop()

    def test_forum_pagination_on_prod(self):
        """Post a new thread and reply to the thread
        Check pagination after 20 posts.
        This test is suppossed to be run only on Production site.
        It Posts in the auto-test forums which is only viewable by certain users
        Note: This test will not run locally by itself. It will only run in BFT suite.
        """
        self.selenium.stop()
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, 'https://support.mozilla.com')
        self.selenium.start()
        self.timeout = vars.ConnectionParameters.page_load_timeout
        self.selenium.set_timeout(self.timeout)
        sel = self.selenium
        #sel.open('https://support.mozilla.com')
        login_page_obj   = login_page.LoginPage(sel)
        forums_page_obj  = forums_page.ForumsPage(sel)
        
        user_info       = sumo_test_data.SUMOtestData().getUserInfo(1)
        uname           = user_info['username']
        pwd             = user_info['password']
        
        ''' Login '''
        login_page_obj.log_in(uname, pwd)
        time.sleep(5)  
        
        #base_url_secure = sel.get_location()[:-10]
        
        ''' Post a new thread '''

        """this forum is only only viewable by certain users,
        so posting to it on Prod is allowed.
        """
        sel.open('https://support.mozilla.com/en-US/forums/auto-test')
        forums_page_obj.post_new_thread_first_cat(self.thread_title, self.thread_text)
        
        #global thread_loc
        self.thread_loc = str(sel.get_location())
        thread_loc_arr = self.thread_loc.split('/')
        url1 = thread_loc_arr[len(thread_loc_arr) - 2]
        url2 = thread_loc_arr[len(thread_loc_arr) - 1]    
        thread_loc = "https://support.mozilla.com/en-US/forums/%s/%s" % (url1, url2)
        
        '''Post over 20 replies'''
        '''Each page takes 20 posts'''
        num_of_posts = 21

        for counter in range(1, (num_of_posts + 1)):
            thread_reply = 'some reply ' + str(int(self.thread_num) + counter)
            forums_page_obj.post_reply(thread_loc, thread_reply)
            self.failUnless(sel.is_text_present(thread_reply),
                "%s not present on %s" % (thread_reply, thread_loc))
            '''Once there are over 20 posts, verify pagination'''
            '''Verify for new page/previous page links '''
            if(counter > 20 and counter % 20 == 1):
                self.failUnless(
                    sel.is_element_present(forums_page_obj.pagination_link),
                    "Pagination not present at %s" % sel.get_location())
                '''If counter=41 then previous page = page 2 '''
                prev_page_num = int((counter - 1) / 20)
                prev_page_link = thread_loc
                prev_page_link += '?page=' + str(prev_page_num)
                self.failUnless(sel.is_element_present(
                    'css=a[href*=' + prev_page_link + ']'),
                    "Prev page link of %s not present at %s" %
                    (prev_page_link, sel.get_location()))
                sel.click('css=a[href=' + prev_page_link + ']')
                sel.wait_for_page_to_load(
                    vars.ConnectionParameters.page_load_timeout)
                self.failUnless(
                    sel.is_element_present(forums_page_obj.next_page_link))
                next_page_num = prev_page_num + 1
                next_page_link = thread_loc
                next_page_link += '?page=' + str(next_page_num)
                self.failUnless(sel.is_element_present(
                    'css=a[href=' + next_page_link + ']'),
                    "next page link not present")
        
if __name__ == "__main__":
    unittest.main()                                               