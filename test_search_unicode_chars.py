# -*- coding: latin-1 -*-

'''
Created on Apr 1, 2011

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import search_page
import refine_search_page

class SearchUnicodeChars(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

    def test_search_unicode_chars(self):
        sel = self.selenium
        search_page_obj       = search_page.SearchPage(sel)
        refine_search_page_obj     = refine_search_page.RefineSearchPage(sel)
                
        search_terms = [u"benötigt"]
        for current_search_term in search_terms:
            refine_search_page_obj.go_to_refine_search_page()
            refine_search_page_obj.do_search_on_support_questions(current_search_term, search_page_obj)
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
            if search_page_obj.is_result_present():
                self.failUnless(sel.is_text_present(current_search_term), "%s not present in search results " %(current_search_term))

        
 

if __name__ == "__main__":
    unittest.main()