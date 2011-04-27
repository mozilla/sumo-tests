from selenium import selenium
import vars
import unittest
import sumo_functions


class hp_see_all_pop_support_articles(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_hp_see_all_pop_support_articles(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/en-US/kb/")
        URL_name = sel.get_location()
        sel.click("button-seeall")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        url = URL_name + "Article+list"
        self.failUnless(url in sel.get_location(),
            "%s not in %s" % (url, sel.get_location))
        #self.failUnless(sel.is_text_present(
        #    "Here is a list of all Knowledge Base topics"),
        #    "header not present")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
