from selenium import selenium
import vars
import unittest
import search_page


class cant_find_what_youre_looking_for_test(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_cant_find_what_youre_looking_for_test(self):
        sel = self.selenium
        search_page_obj       = search_page.SearchPage(sel)
        
        searchTerms = ["firefox", "bgkhdsaghb"]
        for current_search_term in searchTerms:
            search_page_obj.go_to_search_page()
            search_page_obj.do_search_on_search_box(current_search_term)
#            
#            try:
#                sel.click("css=div#basic-search > form > input[type='submit']")
#                sel.wait_for_page_to_load(
#                vars.ConnectionParameters.page_load_timeout)
#            except:
#                pass
            self.failUnless(search_page_obj.is_text_present(
                "Can't find what you're looking for?"),
                "Can't find text not present")
            self.failUnless(search_page_obj.is_element_present(
                "link=Ask a support question instead!"),
                "Ask question link not present")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
