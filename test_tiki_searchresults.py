from selenium import selenium
import vars
import unittest
import sumo_functions


class tiki_searchresults(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_tiki_searchresults(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)

        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/en-US/kb/")
        sel.type("fsearch-new", "firefox crashes")
        sel.click("searchsubmit-new")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        not_found = True
        counter = 1
        while(not_found and counter < 3):
            if(not(sel.is_element_present("link=2"))):
                sel.refresh()
                sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                counter = counter+1
            else:
                not_found = False
        self.failUnless(sel.is_element_present("link=2"))
        self.failUnless(sel.is_element_present("link=Next"))
        self.assertEqual("firefox crashes", sel.get_value("q"))
        sel.click("css=input[value='Search']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_element_present(
            "css=div#content > ol > li > a"),
            "Result not present")
        self.failUnless(sel.is_element_present(
            "link=Ask a support question instead!"))
        self.failUnless(sel.is_element_present(
            "css=ul#side-menu > li > h3 > a"),
            "Sidebar links not present")
        self.failUnless(sel.is_element_present("link=Knowledge Base"))
        self.failUnless(sel.is_element_present("link=Support Forum"))
        self.failUnless(sel.is_element_present("link=Ask a Question"))
        self.failUnless(sel.is_element_present("link=Other Firefox Support"))
        self.failUnless(sel.is_element_present("link=How to Contribute"))

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
