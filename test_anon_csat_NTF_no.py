from selenium import selenium
import unittest
import sumo_functions
import vars


class anon_csat_NTF_no(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_anon_csat_ntf_no(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        # This testcase verified that clicking "no" for both questions
        # in the CSAT poll works as expected
        sumo_func.open(sel, "/en-US/kb/Firefox+Support+Home+Page")
        sel.click("css=div#promotebox-list a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.click("css=input[value='No']")
        sel.click("css=div#pollarea2 div#polledit input:nth-child(2)")
        self.failIf(sel.is_visible("polls_optionId"), "Poll is still visible")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
