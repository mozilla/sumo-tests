import random
from selenium import selenium
import unittest
import forums_page
import login_page
import sumo_test_data
import vars
import re


class ForumDeletion(unittest.TestCase):

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

    def test_forum_deletion(self):
        '''Checks bug 569310 (accidental forum deletion)'''
        sel = self.selenium
        login_page_obj   = login_page.LoginPage(sel)
        forums_page_obj  = forums_page.ForumsPage(sel)
        
        user_adm = 1
        thread_num = str(random.randint(100, 10000))
        user_info       = sumo_test_data.SUMOtestData().getUserInfo(user_adm)
        uname           = user_info['username']
        pwd             = user_info['password']
        
        ''' Login '''
        login_page_obj.log_in(uname, pwd)       
        
        ''' Post a new thread '''

        thread_title = 'test_thread_' + thread_num
        thread_text = 'some text'
        ''' Post a new thread '''
        forums_page_obj.go_to_forums_cat_list_page()
        forums_page_obj.click(forums_page_obj.first_cat_forum_link,True)
        forums_page_obj.post_new_thread_first_cat(thread_title,thread_text)
               
        thread_loc = str(sel.get_location())
        thread_loc_arr = thread_loc.split('/')
        url1 = thread_loc_arr[len(thread_loc_arr) - 2]
        url2 = thread_loc_arr[len(thread_loc_arr) - 1]    
        thread_loc = vars.ConnectionParameters.baseurl_ssl+'/en-US/forums/%s/%s' % (url1, url2)

        num_of_posts = 5

        for counter in range(1, (num_of_posts + 1)):
            thread_reply = 'some reply %s' % str(int(thread_num) + counter)
            forums_page_obj.post_reply(thread_loc, thread_reply)
            
        location = sel.get_location()
        p = re.compile('post-[0-9]*')
        postString = p.search(location)
        postNum = postString.group()[5:]
        # delete link of second to last post
        sel.click("css=li#post-%s > div > div > a:nth-child(2)"
            % str(int(postNum) - 1))
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        #confirmation dialogue for deletion
        sel.click("css=form > input[type='submit']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.open(thread_loc)
        self.failUnless(sel.is_text_present(thread_title))

if __name__ == "__main__":
    unittest.main()
