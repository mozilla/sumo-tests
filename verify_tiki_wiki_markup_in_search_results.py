from selenium import selenium
from vars import *
import unittest, time, re

class verify_tiki_wiki_markup_in_search_results(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium(server, port, browser, baseurl)
        self.selenium.start()
    
    def test_verify_tiki_wiki_markup_in_search_results(self):
        sel = self.selenium
        # Store some needed variables
        searchTerms = sel.get_eval("searchTerms = new Array(\"crashes\",\"firefox crashes\");")
        # This is probably the ugliest JS array ever:
        regExpList = sel.get_eval("regExpList = new Array(\"#^\\!+#m\",\"#^;:#m\",\"/\\{maketoc\\}/Ui\",\"#\\{ANAME.*?ANAME\\}#\",\"/__/\",\"/\\^(.*?)\\^/\",\"/\\{[a-zA-Z]+.*\\}/U\",\"#~/?np~#\",\"/~(h|t)c~.*\\~\\/\\1c~/U\",\"/\\(\\((.*)(?:\\|(.*))?\\)\\)/Ue\",\"#\\[.+\\|(.+)\\]#U\",\"#\\'\\'#\",\"#%{2,}#\");")
        i = 0
        # For each search term in the array do:
        # sel.while("${i}<2")
        while i < 2:
            currentTerm = sel.get_eval("searchTerms[" + str(i) + "]")
            i = i + 1
            sel.open("/search")
            # Click the search field and enter the search terms
            sel.type("q", currentTerm)
            sel.click("//div[@id='basic-search']/form/input[@type='submit']")
            sel.wait_for_page_to_load("30000")
            # Verify that there are 10 results on the page
            # After that, click the "Next" link, until we're at the end of the search results:
            isNextLinkPresent = sel.is_element_present("link=Next")
            # sel.while("${isNextLinkPresent}==true")
            while isNextLinkPresent:
                x = 1
                # sel.while("${x}<13")
                while x < 13:
                    currentRegExp = sel.get_eval("regExpList[" + str(x) + "]")
                    x = x + 1
                    print("DEBUG: Current RegExp: " + currentRegExp)
                    self.failIf(sel.is_element_present("//div[@class=\"search-results\"]/div/p[contains( . ,\"" + currentRegExp + "\")]"))
                # sel.end_while()
                sel.click("link=Next")
                sel.wait_for_page_to_load("30000")
                # Verify that we have a Next link on this page, otherwise, we're at the end of the results and don't need to count the results anymore!
                isNextLinkPresent = sel.is_element_present("link=Next")
            # sel.end_while()
        # sel.end_while()
    
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
