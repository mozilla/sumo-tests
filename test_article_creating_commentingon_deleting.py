from selenium import selenium
import vars
import unittest
import sumo_functions
import urllib
import time
import sumo_test_data
import random

class article_creating_commentingon_deleting(unittest.TestCase):

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

    def test_article_creating_commentingon_deleting(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        """ login with an Admin account as he can delete the article """
        self.functions.login(1, sel)
        random_num = random.randint( 1000, 9999)
        article_name = str("test_article_%s" %(random_num))
        sumo_func.open(sel,
            "/tiki-editpage.php?page="+article_name+"&quickedit=Edit")
        sel.type("editwiki",
            "{SHOWFOR(spans=on)/}\n\nDescribe what the article is about here. \
            Include links to pages that users\nmight have mistaken this \
            article for.\n\nDescribe the cause of the problem. Summarize \
            the fix in one sentence.\n\n{maketoc}\n\n\n!Section one title\n \
            Text here.\n# Step 1\n# Step 2\n# Step 3\n# Step 4\n\n!Section \
            two\nText here.\n\njust a test!")
        sel.type("comment", "test")
        self.failUnless(sel.is_text_present("Edit: "+article_name),
            "Edit title not present")
        sel.click("css=div#categorizator input[value='3']")
        self.assertEqual("on",
            sel.get_value("css=div#categorizator input[value='3']"))
        sel.click("preview")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_text_present("Edit: "+article_name),
            "Edit title not present")
        self.failUnless(sel.is_text_present("Preview : "+article_name),
            "Preview title not present")
        self.failUnless(sel.is_text_present(
        "Remember that this is only a preview, and has not yet been saved!"),
            "Preview notice not present")
        self.failUnless(sel.is_text_present("just a test!"),
            "Edited preview text not present")
        sel.click("save")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sumo_func.open(sel, "/kb/"+article_name)
        self.failUnless(sel.is_text_present(article_name),
            "Edited title not present")
        self.failUnless(sel.is_text_present("just a test!"),
            "Edited final text not present")
        sel.type("editpost2", "A new comment!")
        self.failUnless(sel.is_text_present("Post new comment"),
            "Comment button not present")
        sel.click("comments_postComment")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_text_present("A new comment!"),
            "Comment not saved/displayed")
        sel.click("link=remove")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        self.failUnless(sel.is_text_present("Remove page: "+article_name),
            "Remove page title not present")
        self.failUnless(sel.is_text_present("return to wikipage "+article_name),
            "Return to wiki not present")
        self.failUnless(sel.is_text_present(
            "You are about to remove the page "+article_name+" permanently"),
            "Delete warning not present")
        self.failUnless(
            sel.is_text_present("Remove all versions of this page:"),
            "Remove version warning not present")
        sel.click("all")
        sel.click("remove")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        time.sleep(2)
        # selenium doesn't like 404s
        conn = urllib.urlopen(
            vars.ConnectionParameters.authurlssl + "/en-US/kb/"+article_name)
        status = conn.getcode()
        self.failUnless(status == 404)

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
