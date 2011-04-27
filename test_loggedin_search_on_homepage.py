from selenium import selenium
import vars
import unittest
import time
import sumo_functions
import sumo_test_data


class loggedin_search_on_homepage(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
        self.accounts = sumo_test_data.SUMOtestData()
        self.functions = sumo_functions.SUMOfunctions()

    def test_loggedin_search_on_homepage(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()

        self.functions.login(1, sel)
        search_word = "support"
        sumo_func.open(sel, "/en-US/kb/")
        sel.type("q", search_word)
        sel.click("css=input.submit")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        not_found = True
        counter = 1
        while(not_found and counter < 5):
            if(not(sel.is_text_present(search_word))):
                sel.refresh()
                sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                time.sleep(4)
                counter = counter+1
            else:
                not_found = False
        self.failUnless(sel.is_text_present(search_word),
            "search query not present")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
