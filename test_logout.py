from selenium import selenium
import vars
import unittest
import sumo_functions
import sumo_test_data


class logout(unittest.TestCase):

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

    def test_logout(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        user = self.accounts.getUserInfo(2)
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/en-US/kb/")
        self.functions.login(2, sel)
        self.assertEqual("Contributor Home Page", sel.get_title())
        self.failUnless(sel.is_text_present("Contributor Home Page"),
            "Contributor title not present")
        self.failUnless(sel.is_text_present("Log Out"),
            "Logout link missing")
        sel.click("link=Log Out")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.assertEqual("Firefox Support Home Page", sel.get_title())
        self.failUnless(sel.is_text_present("log in"),
            "login link missing")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
