from selenium import selenium
import vars
import unittest
import time
import sumo_functions


class advanced_search_checked_kb_and_forum(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_advanced_search_checked_kb_and_forum(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        # This script checks that the KB tickbox is checked
        # and that the default forum to search is "Firefox"
        sumo_func.open(sel, "/search?a=2")
        self.failUnless(sel.is_checked("id_category_0"),
                       "Default search forum is not set to Firefox")
        search_word = "Firefox crashes"
        sel.type("kb_q", search_word)
        #submit search
        #sel.click("css=form.kb > div.submit-search > input")
        sel.click("css=input[value='Search']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        not_found = True
        counter = 1
        while(not_found and counter < 5):
            if(not(sel.is_text_present(search_word))):
                sel.refresh()
                sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                time.sleep(1)
                counter = counter+1
            else:
                not_found = False
        self.failUnless(
        sel.is_element_present("css=div.search-results > div.result > a"),
                               "Search result at %s on page %s not found" %
                               ("css=div.search-results > div.result > a",
                               sel.get_location()))
        sumo_func.open(sel, "/search?a=2")
        #switch tabs
        sel.click("css=div#search-tabs > ul > li:nth-child(2) > a")
        search_word = "Firefox crashes"
        sel.type("support_q", search_word)
        #submit search
        sel.click("css=div.submit-search > input")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        not_found = True
        counter = 1
        while(not_found and counter < 5):
            if(not(sel.is_text_present(search_word))):
                sel.refresh()
                sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                time.sleep(1)
                counter = counter+1
            else:
                not_found = False
        self.failUnless(sel.is_element_present(
                        "css=div.search-results > div.result > a"))

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
