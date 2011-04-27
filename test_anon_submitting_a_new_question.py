from selenium import selenium
import vars
import unittest
import datetime
import time

import sumo_functions


class anon_submitting_a_new_question(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_anon_submitting_a_new_question(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        timestamp = sel.get_eval("new Date().getTime()")
        sumo_func.open(sel, "/en-US/kb/Firefox+Support+Home+Page")
        sel.click("link=2) Get Personal Help")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.click("link=Ask a new question in the forum")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        
        sel.click("css=ul.select-one > li > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.click("css=ul.select-one > li > a")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        question_to_ask = "automation test question %s" %(datetime.date.today())
        sel.type("search", question_to_ask)
        sel.click("css=input[value='Ask this']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.click("css=input[value *='None']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.type("id_content", "This is a test. " + timestamp)
        sel.type("id_troubleshooting", "troubleshooting info")
        sel.click("css=input[value='Post Question']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        sel.type("id_email", "abc@abc.com")
        sel.click("css=input[value='Post Question']")
        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        time.sleep(3)
        self.failUnless(sel.is_text_present(question_to_ask), "Did not find posted Question %s \r\n" %(question_to_ask))
        
        
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
