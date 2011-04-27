from selenium import selenium
import vars
import unittest
import refine_search_page


class SearchTagsOnly(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
            vars.ConnectionParameters.server,
            vars.ConnectionParameters.port,
            vars.ConnectionParameters.browser,
            vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_search_only_tags_dont_return_zero(self):
        """ Checks advanced question search with only tags to ensure nonzero result (bug 583156) """
        refine_search_page_obj = refine_search_page.RefineSearchPage(self.selenium)
        
        search_terms = ["desktop"]
        for current_search_term in search_terms:
            refine_search_page_obj.go_to_refine_search_page()
            refine_search_page_obj.do_search_tags_on_support_questions(
                current_search_term, refine_search_page_obj)
            self.assertFalse(refine_search_page_obj.is_text_present(
                "Found 0 results"),
                "Found 0 results")

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
