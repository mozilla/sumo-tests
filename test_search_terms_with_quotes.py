from selenium import selenium
import unittest

import vars
import search_page

class SearchTermsWithQuotes(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_search_terms_with_quotes(self):
        sel = self.selenium
        search_page_obj       = search_page.SearchPage(sel)
        
        searchTerms = ["\"bookmark\"", "\"clear history\""]
        for current_search_term in searchTerms:
            search_page_obj.go_to_search_page()
            search_page_obj.do_search_on_search_box(current_search_term)
            self.failUnless(sel.is_element_present(search_page_obj.result_div), "No results for %s" %(current_search_term))

    def test_that_pagination_works_for_search_terms_with_quotes(self):
        """
           tests pagination works for search terms with quotes
           bug 529694
        """
        sel = self.selenium
        search_page_obj       = search_page.SearchPage(sel)
        
        searchTerms = ["\"bookmark\"", "\"clear history\""]
        for current_search_term in searchTerms:
            search_page_obj.go_to_search_page()
            search_page_obj.do_search_on_search_box(current_search_term)
            count = 0
            while(count<5):
                if sel.is_element_present(search_page_obj.next_page_link):
                    search_page_obj.click(search_page_obj.next_page_link, True, vars.ConnectionParameters.page_load_timeout)
                    self.failUnless(sel.is_element_present(search_page_obj.result_div), "No results for %s" %(current_search_term))
                    count = count + 1
                else:
                    break

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
