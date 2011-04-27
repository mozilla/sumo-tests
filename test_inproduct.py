from selenium import selenium
import vars
import unittest
import sumo_functions


class inproduct(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_inproduct(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()

        sumo_func.open(sel, "/en-US/kb/Firefox+Help?style_mode=inproduct")
        if sel.is_text_present('Page Not Found'):
            return
        self.failUnless(sel.is_element_present("q"),
            "Search box not present")
        # Checks search box is present
        self.failUnless(sel.is_text_present("Firefox Help"),
            "FF help text not present")
        # Checks "How to contribute link"
        self.failUnless(sel.is_text_present("Want to contribute"),
            "Contribute text not present")
        # Checks the lead up to the quick search buttons
        self.failUnless(sel.is_text_present("New to Firefox?"),
            "new to firefox widget missing")
        # Checks "New to Firefox?" widget is shown
        self.failUnless(sel.is_text_present("Need Help With*"),
            "need help text missing")
        # Checks link to all articles is shown
        self.failUnless(sel.is_element_present("css=a[href *='/en-US/kb/']"),
            "Not a single KB article link present")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
