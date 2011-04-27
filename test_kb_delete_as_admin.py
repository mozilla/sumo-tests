from selenium import selenium
import vars
import unittest
import sumo_functions
import urllib
import sumo_test_data


class kb_delete_as_admin(unittest.TestCase):

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

    def test_kb_delete_as_admin(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        user = self.accounts.getUserInfo(1)
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        sumo_func.open(sel, "/en-US/kb/Firefox+Support+Home+Page")
        self.functions.login(1, sel)
        sel.click("link=Create an article")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.type("page", "deletiontesting")
        sel.click("quickedit")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # types "deletiontesting" into the body
        # of the article
        sel.type("editwiki", "deletiontesting")
        # types a comment for the article
        sel.type("comment", "testing article with quotes. \"Quotes.\"")
        # adds some tags
        sel.type("tagBox", "article, deletion, quotes")
        # submits the article
        sel.click("save")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # verifies all the stuff we've entered
        self.failUnless(
            "This is a new staging page that has not been approved" in
            sel.get_text("css=div#col1 > div > div > div:nth-child(3)"))
        self.failUnless(sel.is_text_present("deletiontesting"),
            "content text not present")
        self.failUnless(sel.is_text_present("article"),
            "tags not working")
        self.failUnless(sel.is_text_present("quotes"),
            "tags not working")
        # remove the article
        sel.click("link=remove")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(
            sel.is_element_present("link=return to wikipage deletiontesting"),
            "wikipage return link not present")
        sel.click("remove")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_text_present("Need Help with Firefox?"),
            "remove redirect failed")
        # we're still logged in, right?
        self.failUnless(sel.is_element_present("link=log out"),
            "no longer logged in")
        # log out
        self.functions.logout(sel)
        #selenium RC does not like 404 responses
        conn = urllib.urlopen(vars.ConnectionParameters.authurlssl +
            "/en-US/kb/deletiontesting")
        status = conn.getcode()
        self.failUnless(status == 404)

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
