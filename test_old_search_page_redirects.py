from selenium import selenium
import vars
import unittest
import sumo_functions


class old_search_page_redirects(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_old_search_page_redirects(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        #check redirect from old tiki search
        sumo_func.open(sel,
            "/tiki-newsearch.php?where=all&locale=en-US&q=shockwave&sa=Search")
        self.failUnless("/search?" in sel.get_location(),
            "%s incorrect redirection" % sel.get_location())
        self.failUnless("q=shockwave" in sel.get_location(),
            "%s incorrect redirection" % sel.get_location())
        #check redirect from old php search
        sumo_func.open(sel, "/search.php?q=shockwave&locale=en-US&where=all")
        self.failUnless("/search?" in sel.get_location(),
            "%s incorrect redirection" % sel.get_location())
        self.failUnless("q=shockwave" in sel.get_location(),
            "%s incorrect redirection" % sel.get_location())

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
