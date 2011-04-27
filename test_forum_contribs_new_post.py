from selenium import selenium
import vars
import unittest
import sumo_functions
import sumo_test_data
import time

class forum_contribs_new_post(unittest.TestCase):

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

    def test_forum_contribs_new_post(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()

        # Timestamp allows unique value each run
        Timestamp = sel.get_eval("new Date().getTime()")
        postTitle = "Litmus 7829 test" + Timestamp
        #postSumm = "Litmus Sel Test 9533"
        postMsg = "Litmus QA Testcase Test Msg"

        self.functions.login(0, sel)

        # we are using ssl url to preserver login info
        sumo_func.open(sel, vars.ConnectionParameters.baseurl_ssl+"/en-US/forums/contributors")
        #self.assertEqual("Contributors | Forums | Firefox Support",
            #sel.get_title())
        sumo_func.open(sel, sel.get_location() + "/new")
        sel.type("css=form.new-thread input#id_title", postTitle)
        sel.type("css=form.new-thread textarea#id_content", postMsg)
        sel.click("css=input[value='Post']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        time.sleep(5)
        self.failUnless(sel.is_text_present(postMsg))
        # Verify post title
        sumo_func.open(sel, vars.ConnectionParameters.baseurl_ssl+"/en-US/forums/contributors")
        self.failUnless(sel.is_text_present(postTitle))
        '''
        # Verify this post is not present in other forums
        sumo_func.open(sel, vars.ConnectionParameters.baseurl_ssl+"/en-US/forums/knowledge-base-articles")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # Verify post not present in this forum
        self.failIf(sel.is_text_present(postTitle))

        sel.click("css=ol.breadcrumbs > li:nth-child(2) > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # Click link toOff Topic Forum
        sel.click("link=Off Topic")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # Verify post not present in this forum
        self.failIf(sel.is_text_present(postTitle))

        sel.click("css=ol.breadcrumbs > li:nth-child(2) > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.click("link=Contributors")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # verify post is present in this forum
        self.failUnless(sel.is_text_present(postTitle))
        '''
        # Logout
        self.functions.logout(sel)

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
