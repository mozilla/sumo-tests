from selenium import selenium
import vars
import unittest
import sumo_functions
import sumo_test_data


class no_query_adv_forum_search(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_no_query_adv_forum_search(self):
        sel = self.selenium
        user = sumo_test_data.SUMOtestData().getUserInfo(0)
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, "en-US/search?a=2")
        # clicks support form tab
        sel.click("css=div#search-tabs > ul > li:nth-child(2) > a")
        sel.type("id_asked_by", user['username'])
        sel.click("css=form#support input[value='Search']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless("refine" in sel.get_attribute(
            "css=div#basic-search > form > input:nth-child(13)@class"),
            "refine class not found")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
