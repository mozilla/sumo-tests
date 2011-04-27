from selenium import selenium
import vars
import unittest
import sumo_functions


class verify_num_results_on_page(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_verify_num_results_on_page(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        # Store some needed variables
        searchTerms = ["crashes", "firefox crashes"]
        for currentTerm in searchTerms:
            sumo_func.open(sel, "/search")
            # Click the search field and enter the search terms
            sel.type("q", currentTerm)
            sel.click("css=div#basic-search input[type='submit']")
            sel.wait_for_page_to_load(
                vars.ConnectionParameters.page_load_timeout)
            # Verify that there are 10 results on the page
            # After that, click the "Next" link,
            # until we're at the end of the search results:
            counter = 1
            while sel.is_element_present("link=Next") and counter < 11:
                self.assertEqual("10", sel.get_xpath_count(
                "//div[@id='content-inner']/div[3]/div[@class='result']"))
                sel.click("link=Next")
                sel.wait_for_page_to_load(
                    vars.ConnectionParameters.page_load_timeout)
                # Verify that we have a Next link on this page, otherwise,
                # we're at the end of the results and don't need to
                # count the results anymore!
                counter += 1

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
