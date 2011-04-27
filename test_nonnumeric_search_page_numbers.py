from selenium import selenium
import vars
import unittest
import sumo_functions


class nonnumeric_search_page_numbers(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_nonnumeric_search_page_numbers(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        url = "/en-US/search?q=firefox+crashes&page="
        pages = ["string", "2str", "$@&%*", "?2"]
        for page in pages:
            sumo_func.open(sel, url + page)
            self.failUnless(sel.is_element_present("css=div.result > a"), "No search results for non-numeric pages")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
