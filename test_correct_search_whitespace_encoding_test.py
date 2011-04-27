from selenium import selenium
import vars
import unittest
import sumo_functions


class correct_search_whitespace_encoding_test(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_correct_search_whitespace_encoding_test(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        searchTermArray = ["export bookmarks", "clear history",
            "home page", "import bookmarks", "clear cache"]
        for currentSearchTerm in searchTermArray:
            sumo_func.open(sel, "en-US/kb/")
            sel.click("link=" + currentSearchTerm)
            sel.wait_for_page_to_load(
                vars.ConnectionParameters.page_load_timeout)
            self.assertEqual(currentSearchTerm,
                sel.get_attribute("css=div#basic-search > form > input@value"))
            self.assertEqual(currentSearchTerm,
            sel.get_text(
            "css=div#content-inner > div:nth-child(2) > strong:nth-child(2)"))

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
