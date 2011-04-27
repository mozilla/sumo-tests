from selenium import selenium
import vars
import unittest
import sumo_functions
import sumo_test_data


class article_history(unittest.TestCase):

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

    def test_article_history(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        user = self.accounts.getUserInfo(1)
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/")
        self.functions.login(1, sel)
        sel.click("css=div#breadcrumbs a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_element_present("link=Installing Firefox"),
            "Installing Firefox link not present")
        sel.click("link=Installing Firefox")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.assertEqual("Installing Firefox", sel.get_title())
        self.failUnless(sel.is_element_present("link=History"),
            "History link not present")
        sel.click("link=History")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(
            sel.is_element_present("link=exact:History: Installing Firefox"),
            "History: Installing Firefox link not present")
        self.failUnless(sel.is_element_present("link=View page"),
            "View Page link not present")
        sel.click("link=View page")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.assertEqual("Installing Firefox", sel.get_title())

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
