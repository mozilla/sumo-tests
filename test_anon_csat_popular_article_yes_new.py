from selenium import selenium
import vars
import unittest
import sumo_functions


class anon_csat_popular_article_yes_new(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_anon_csat_popular_article_yes_new(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        sumo_func.open(sel, vars.ConnectionParameters.authurl)
        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
        # Testcase verifies answering "yes" for the CSAT questions
        # for KB articles under "Most popular" section.
        poll_option = 1
        while poll_option < 6:
            sumo_func.open(sel, "/en-US/kb/Firefox+Support+Home+Page")
            sel.click("css=div#promotebox-list a")
            sel.wait_for_page_to_load(
                vars.ConnectionParameters.page_load_timeout)
            sel.click("css=div#pollarea input")
            sel.click("css=div#polledit input[value=%s]" % str(poll_option))
            sel.click("polls_submit")
            sel.click("css=div#pollarea2 input")
            self.failIf(sel.is_visible("polls_optionId"), "Poll still visible")
            poll_option = poll_option + 1

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
