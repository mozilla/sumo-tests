from selenium import selenium
import vars
import unittest
import sumo_functions


class how_to_contribute(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_how_to_contribute(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()

        sumo_func.open(sel, "/contribute")
        self.failUnless("superheroes-wanted" in sel.get_location())
        self.failUnless(sel.is_element_present("link=Register"),
            "Create an account link not present")
        self.failUnless(sel.is_element_present(
            "link=Improve*Knowledge*Base"),
            "improve KB link not present")
        self.failUnless(sel.is_element_present(
            "link=*Localize*"),
            "Localize link not present")
        self.failUnless(sel.is_text_present(
            "Firefox support global!"),
            "Global text not present")
        self.failUnless(sel.is_element_present("link=*support*questions"),
            "forum support link not present")
        self.failUnless(sel.is_element_present("link=*Live*Chat"),
            "Help with live chat link not present")
        self.failUnless(sel.is_element_present("link=Contributors Forum"),
            "contributors forum link not present")
        self.failUnless(sel.is_element_present("link=*blog"),
            "sumo blog link not present")
        self.failUnless(sel.is_element_present("link=Quality Assurance"),
            "QA link not present")
        self.failUnless(sel.is_element_present("link=#sumo IRC channel"),
            "sumo irc channel link not present")
        self.failUnless(sel.is_element_present("link=via Mibbit"),
            "mibbit link not present")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
