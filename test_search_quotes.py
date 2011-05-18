'''
Created on Jul 28, 2010

@author: mozilla
'''
import pytest

import search_page

@pytest.mark.smoketests
@pytest.mark.bft
class TestSearchQuotes:

    def test_search_quotes(self, testsetup):
        search_page_obj       = search_page.SearchPage(testsetup)
                
        search_terms = ["\"lost bookmark\"", "\"clear history\""]
        for current_search_term in search_terms:
            search_page_obj.go_to_search_page()
            search_page_obj.do_search_on_search_box(current_search_term)
            not_found = True
            counter = 0
            while(not_found and counter < 3):
                if(not(search_page_obj.is_search_available())):
                    search_page_obj.refresh()
                    counter = counter+1
                else:
                    not_found = False
            assert(search_page_obj.is_element_present(search_page_obj.result_div), "No search results for %s" %(current_search_term))