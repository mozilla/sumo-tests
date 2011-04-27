from selenium import selenium
import vars
import unittest
import sumo_functions


class webtrends_search_tracking(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_webtrends_search_tracking(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, "/en-US/search?q=deleting+bookmarks")
        source = sel.get_html_source()
        if 'WT.oss' in source and 'WT.oss_r' in source:
            name = sel.get_attribute(
                "css=head > meta[name='WT.oss']@content")
            count = sel.get_attribute(
                "css=head > meta[name='WT.oss_r']@content")
            name2 = sel.get_text(
            "css=div#content-inner > div:nth-child(2) > strong:nth-child(2)")
            count2 = sel.get_text(
            "css=div#content-inner > div:nth-child(2) > strong")
            self.failUnless(name == name2, "WT.oss is problematic")
            self.failUnless(count == count2, "WT.oss_r is problematic")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
