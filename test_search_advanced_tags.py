'''
Created on Jul 30, 2010

@author: mozilla
'''
from selenium import selenium
import vars
import unittest
import sumo_functions


class SearchAdvancedTags(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_search_advanced_tags(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, "en-US/search?a=2")
        # clicks support form tab
        sel.click("css=div#search-tabs > ul > li:nth-child(2) > a")
        sel.type("support_q", "desktop")
        sel.click("css=form#support input[value='Search']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_element_present("css=div.result"))

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
