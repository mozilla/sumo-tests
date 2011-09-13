from selenium import selenium
import vars
import unittest
import sumo_functions
import sumo_test_data


class loggedin_translate_existing_article(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
        self.accounts = sumo_test_data.SUMOtestData()
        self.functions = sumo_functions.SUMOfunctions()

    def test_loggedin_translate_existing_article(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        user = self.accounts.getUserInfo(0)
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        timestamp = sel.get_eval("new Date().getTime()")
        language = "hi-IN"
        self.functions.login(sel, 'default')
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sel.click("css=div#mostpopular-new > ul > li:nth-child(6) > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.click("link=Translate this page")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # Selecting a language from drop-down list
        #breaks in IE for all types of selectors
        #sel.select("lang", "index=0")
        sel.type("page", "article_" + timestamp)
        sel.click("css=input[value='Create translation']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.type("editwiki", "article_" + timestamp)
        sel.type("comment", "article_" + timestamp)
        sel.click("save")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sumo_func.open(sel, "/en-US/kb/article_" + timestamp + "?bl=n")
        # Logging out
        sel.click("link=Log Out")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sumo_func.open(sel, "/en-US/kb/")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
