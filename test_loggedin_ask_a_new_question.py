from selenium import selenium
import vars
import unittest
import datetime
import time
import sumo_functions
import sumo_test_data


class loggedin_ask_a_new_question(unittest.TestCase):

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

    def test_loggedin_ask_a_new_question(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        # Description: This testcase verifies adding a new question
        timestamp = sel.get_eval("new Date().getTime()")
        self.functions.login(0, sel)
        sumo_func.open(sel, '/')
        sel.open("/en-US/kb/ask")
        sel.click("link=Ask a new question in the forum")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        # Adding a new question
        sel.click("css=ul.select-one > li > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.click("css=ul.select-one > li > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        question_to_ask = "automation test question %s" %(datetime.date.today())
        sel.type("search", question_to_ask)
        sel.click("css=input[value='Ask this']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.click("show-form-btn")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.type("id_content", "This is a test. " + timestamp)
        sel.type("id_troubleshooting", "troubleshooting info")
        sel.click("css=input[value='Post Question']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        time.sleep(3)
        self.failUnless(sel.is_text_present("Your question has been posted"), "Did not get confirmation for Question: %s \r\n" %(question_to_ask))
        self.failUnless(sel.is_text_present(question_to_ask))

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
