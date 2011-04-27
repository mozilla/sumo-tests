from selenium import selenium
import vars
import unittest
import sumo_functions
import sumo_test_data


class login2x(unittest.TestCase):
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

    def test_login2x(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/en-US/kb/")
        self.functions.login(0, sel)
        self.assertEqual("Contributor Home Page", sel.get_title())
        self.failUnless(sel.is_text_present("Contributor Home Page"),
            "contributor title missing")
        # Now bring up the already logged in screen
        sumo_func.open(sel, "/tiki-login_scr.php")
        # Verify the already logged in text
        self.failUnless(sel.is_element_present("css=div#mod-login_box > div"),
            "login box missing")
        self.failUnless(sel.is_text_present("Logged in as:"),
            "not logged in")
        # Click the log out in msg prompt
        sel.click("link=Log out")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.assertEqual("Firefox Support Home Page", sel.get_title())

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
