from selenium import selenium
import vars
import unittest
import sumo_functions


class kb_static(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_kb_static(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)

        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/en-US/kb/")
        self.assertEqual("Firefox Support Home Page", sel.get_title())
        # Checks text above search box
        self.failUnless(sel.is_text_present("What do you need help with?"),
            "what need help not present")
        self.failUnless(sel.is_text_present("New to Firefox?"),
            "new to firefox not present")
        # Checks the "new to firefox?" text shows
        self.failUnless(sel.is_text_present("Popular Support Articles"),
            "pop support articles not present")
        self.failUnless(sel.is_element_present("button-seeall"),
            "see all articles link not present")
        self.failUnless(sel.is_text_present("Thunderbird Support"),
            "thunderbird support text not present")
        # Checks link to Thunderbird is shown ( footer )
        self.failUnless(sel.is_element_present("link=Thunderbird"),
            "thunderbird link not present")
        self.failUnless(sel.is_element_present("link=More"),
            "more link not present")
        # Checks link to tiki-browse_freetags.php
        self.failUnless(sel.is_element_present("search-try"),
            "search box not present")
        # Checks search box area is present
        self.failUnless(sel.is_element_present("promotebox-title"),
            "promote widget not present")
        # This checks the promote widget is showing ( "new to firefox" )
        self.failUnless(sel.is_element_present(
            "css=div#waysgethelp-list > ul > li"),
            "search ff ways to get help not present")
        self.assertEqual("4", sel.get_xpath_count(
            "//div[@id=\"promotebox-list\"]/ul/li/a"))
        # This checks there a 4 links under "New to Firefox?"
        self.failUnless(sel.is_element_present("wantgetinvolved-title"),
            "want to get involved widget not present")
        # This checks the "want to get involved" widget shows
        self.failUnless(sel.is_element_present("waysgethelp-title"),
            "ways to help widget missing")
        # Checks that the "ways to help" widget shows
        self.failUnless(sel.is_element_present(
            "link=2) Get Personal Help"),
            "get personal help link missing")
        self.failUnless(sel.is_element_present(
            "link=3) Other Firefox Support"),
            "other ff support link missing")
        # The above check links under "ways to get help"
        self.failUnless(sel.is_element_present(
            "link=Find out how to contribute"),
            "find out how to contribute link missing")
        # Checks the how to contribute link under "want to get involved?"
        self.failUnless(sel.is_element_present("link=log in"),
            "login link missing")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
