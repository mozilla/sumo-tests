from selenium import selenium
import vars
import unittest

import search_page


class verify_tiki_wiki_markup_in_search_results(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_verify_tiki_wiki_markup_in_search_results(self):
        sel = self.selenium
        search_page_obj       = search_page.SearchPage(sel)
        
        # Store some needed variables
        searchTerms = ["crashes", "firefox crashes"]
        # This is probably the ugliest JS array ever:
        regExpList = ["#^\\!+#m", "#^;:#m", "/\\{maketoc\\}/Ui",
            "#\\{ANAME.*?ANAME\\}#", "/__/", "/\\^(.*?)\\^/",
            "/\\{[a-zA-Z]+.*\\}/U", "#~/?np~#", "/~(h|t)c~.*\\~\\/\\1c~/U",
            "/\\(\\((.*)(?:\\|(.*))?\\)\\)/Ue", "#\\[.+\\|(.+)\\]#U",
            "#\\'\\'#", "#%{2,}#"]
        for currentTerm in searchTerms:
            search_page_obj.go_to_search_page()
            # Click the search field and enter the search terms
            search_page_obj.do_search_on_search_box(currentTerm)

            # Verify that there are 10 results on the page
            # After that, click the "Next" link, until we're at the end
            # of the search results:
            counter = 1
            while sel.is_element_present("link=Next") and counter <= 6:
                for currentRegExp in regExpList:
                    #print("DEBUG: Current RegExp: " + currentRegExp)
                    self.failIf(sel.is_element_present(
                    "//div[@class=\"search-results\"]/div/p[contains( . ,\"" +
                    currentRegExp + "\")]"),
                    "Results contained %s" % currentRegExp)
                sel.click("link=Next")
                sel.wait_for_page_to_load(
                    vars.ConnectionParameters.page_load_timeout)
                # Verify that we have a Next link on this page, otherwise,
                # we're at the end of the results and don't need to count
                # the results anymore!
                counter += 1

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
