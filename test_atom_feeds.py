from selenium import selenium
import vars
import unittest
import sumo_functions
import sys


class atom_feeds(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_atom_feeds(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, "/en-US/forums")
        sel.click("css=div.name > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        forumlink = sel.get_location() + "/feed"
        sel.click("css=div#content-inner div.title a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        threadlink = sel.get_location() + "/feed"
        # selenium will give an XHR error with response_code = 404
        # if page not found, causing failure of test
        
        self.failUnless(sumo_func.getResponse(threadlink) == 200)
        self.failUnless(sumo_func.getResponse(forumlink) == 200)
        #sel.open(threadlink)
        #sel.open(forumlink)

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
