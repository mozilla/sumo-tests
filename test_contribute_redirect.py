from selenium import selenium
import vars
import unittest
import sumo_functions
import urllib

class contribute_redirect(unittest.TestCase):
    
    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
        
    def test_contribute_redirect(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, "/contribute")
        actualUrl = urllib.unquote(sel.get_location())
        self.failUnless("superheroes-wanted" in actualUrl,
            "Redirection failed")
        
    def tearDown(self):
        self.selenium.stop()
        


if __name__ == "__main__":
        unittest.main()
        