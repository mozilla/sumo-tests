from selenium import selenium
import vars
import unittest
import sumo_functions


class ask_a_question(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_ask_a_question(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()

        # Description: This checks that the correct elements and
        # links are shown on the "Ask A Question" page
        sumo_func.open(sel, "/en-US/kb/ask")
        #self.failUnless(sel.is_element_present("css=div#breadcrumbs a"),
            #"Firefox breadcrumb not present")
        self.failUnless(sel.is_text_present("Where to ask your question"),
            "Where to ask your question not present")
        self.failUnless("Ask a question" in sel.get_title())
        self.failUnless(sel.is_text_present("Ask a question"),
            "Ask a question not present")
        self.failUnless(sel.is_element_present("css=div[id='firefox-help']"),
            "Search box header not present")
        self.failUnless(sel.is_element_present("q"),
            "Search box not present")
        self.failUnless(sel.is_element_present("link=Thunderbird Support"),
            "Thunderbird support link not present")
        self.failUnless(sel.is_element_present("link=*forum*"),
            "Forum link not present")
        self.failUnless(sel.is_element_present("link=Other Firefox support"),
            "Other FF Support link not present")
        self.failUnless(sel.is_text_present("Firefox support forum"),
            "FF Support forum link not present")
        self.failUnless(
            sel.is_element_present("link=Ask a new question in the forum"),
            "New Question link not present")
        self.failUnless(sel.is_text_present("Firefox support live chat"),
            "Live chat title not present")
        self.failUnless(
            sel.is_element_present("link=Take me to the live chat"),
            "Live chat link not present")
        self.failUnless(sel.is_text_present("Other places to ask for help"),
            "Other help not present")
        self.failUnless(sel.is_element_present(
            "link=Firefox Help Home"),
            "Sidebar Firefox Support link not present")
        self.failUnless(sel.is_element_present("link=Discussion"),
            "KB DIscussion link not present")
        #self.failUnless(sel.is_element_present("link=Support Forum"),
            #"Support Forum link not present")
        self.failUnless(sel.is_element_present("link=Ask a Question"),
            "Ask a question link not present")
        #self.failUnless(sel.is_element_present("link=How to Contribute"),
            #"How to contribute link not present")
        self.failUnless(sel.is_element_present("link=Sign In") or
            sel.is_element_present("link=Log Out"))

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
