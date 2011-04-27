from selenium import selenium
import vars
import unittest
import sumo_functions
import sumo_test_data


class article_rename_cancel(unittest.TestCase):

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

    def test_article_rename_cancel(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        self.functions.login(0, sel)
        sumo_func.open(sel, "/en-US/kb/Creating+articles")
        self.failUnless(sel.is_text_present("Quick edit an article"),
            "Quick Edit an article text not present")
        sel.type("page", "My First Testing Article")
        self.failUnless(sel.is_element_present("quickedit"),
            "quickedit element not present")
        sel.click("quickedit")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.type("editwiki", "{SHOWFOR(spans=on)/}\n\nDescribe what the \
        article is about here. Include links to pages that users\nmight \
        have mistaken this article for.\n\nDescribe the cause of the \
        problem. Summarize the fix in one sentence.\n\n{maketoc}\n\n\n!\
        Section one title\nText here.\n# Step 1\n# Step 2\n# Step 3\n# \
        Step 4\n\n!Section two\nText here.\n\nI must make sure that \
        MYSECRETWORD is included in this article.")
        sel.type("comment", "I have made new article for testing")
        self.assertEqual("My First Testing Article", sel.get_title())
        self.failUnless(sel.is_text_present(
            "exact:Edit: My First Testing Article"),
            "edit title not present")
        self.failUnless(sel.is_element_present("save"),
            "save element not present")
        sel.click("save")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.assertEqual("My First Testing Article", sel.get_title())
        self.failUnless(sel.is_text_present("My First Testing Article"),
            "title not present")
        self.failUnless(sel.is_text_present(
        "I must make sure that MYSECRETWORD is included in this article."),
        "Content not present")
        self.failUnless(sel.is_element_present("link=rename"),
            "rename link not present")
        sel.click("link=rename")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_element_present(
            "link=My First Testing Article"), "Article link not present")
        self.failUnless(sel.is_element_present("rename"),
            "rename not present")
        sel.click("link=My First Testing Article")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.assertEqual("My First Testing Article", sel.get_title())
        self.failUnless(sel.is_text_present(
            "I must make sure that MYSECRETWORD is included in this article."),
            "Content text not present")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
