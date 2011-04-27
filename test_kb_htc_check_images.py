from selenium import selenium
import vars
import unittest
import sumo_functions


class kb_htc_check_images(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_kb_htc_check_images(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/en-US/kb")
        sel.click("css=div#wantgetinvolved > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_visible(
            "css=div#top > div > a > span.img > img"))

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
