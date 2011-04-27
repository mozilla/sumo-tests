import random
import time
from selenium import selenium
import unittest
import sumo_functions
import vars
import sumo_page


class forum_goto_post_after_reply(unittest.TestCase):

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

    def test_forum_goto_post_after_reply(self):
        '''Checks if forum redirects to post after replying'''
        sel = self.selenium
        sumo_page_obj = sumo_page.SumoPage(sel)
        self.sumo_fncs = sumo_functions.SUMOfunctions()

        userAdm = 1
        thread_num = str(random.randint(100, 10000))
        self.sumo_fncs.login(userAdm, sel)
        # using SSL url to preserve login info
        sumo_page_obj.open(vars.ConnectionParameters.baseurl_ssl+"/en-US/forums")
        sumo_page_obj.click("css=div.name a",True,vars.ConnectionParameters.page_load_timeout)
        sumo_page_obj.click("new-thread",True,vars.ConnectionParameters.page_load_timeout)
        thread_name = 'test_thread_%s' % thread_num
        sel.type("id_title", thread_name)
        thread_text = 'some text'
        sel.type("id_content", thread_text)
        sumo_page_obj.click("css=input[value='Post']",True,vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_text_present(thread_name),
            "Thread name not present")
        self.failUnless(sel.is_text_present(thread_text),
            "Thread text not present")
        thread_loc = str(sel.get_location())
        thread_loc_arr = thread_loc.split('/')
        url1 = thread_loc_arr[len(thread_loc_arr) - 2]
        url2 = thread_loc_arr[len(thread_loc_arr) - 1]
        thread_loc = '/en-US/forums/%s/%s' % (url1, url2)
        num_of_posts = 5
        start_time = time.time()
        for counter in range(1, (num_of_posts + 1)):
            thread_reply = 'some reply %s' % str(int(thread_num) + counter)
            sel.type("id_content", thread_reply)
            sumo_page_obj.click("css=input[value='Reply']",True,vars.ConnectionParameters.page_load_timeout)
            self.failUnless(sel.is_text_present(thread_reply),
                "Thread reply not present")
        location = sel.get_location()
        self.failUnless("#post-" in location,
            "Not redirecting to post (not in url)")

if __name__ == "__main__":
    unittest.main()
