from selenium import selenium
import vars
import unittest
import time
import sumo_functions


class anon_search_on_homepage(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_anon_search_on_homepage(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/en-US/kb/")
        search_word = "support"
        sel.type("fsearch-new", search_word)
        sel.click("searchsubmit-new")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        not_found = True
        counter = 1
        while(not_found and counter < 5):
            if(not(sel.is_text_present(search_word))):
                sel.refresh()
                sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                time.sleep(2)
                counter = counter+1
            else:
                not_found = False
        time.sleep(3)
        self.failUnless(sel.is_text_present(search_word),
            "search text not present")
        #sumo_func.open(sel, "/en-US/kb/")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
