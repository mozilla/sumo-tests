'''
Created on Aug 12, 2010

@author: mozilla
'''

import pytest

import search_page

class TestSearchDecoding:

    @pytest.mark.smoketests
    @pytest.mark.bft
    def test_search_decoding(self, testsetup):
        sel                   = testsetup.selenium
        search_page_obj       = search_page.SearchPage(testsetup)
        
        search_term = "%3D"  
        search_page_obj.go_to_search_page()     
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        self.assertNotEqual("=", sel.get_value(search_page_obj.search_box))
        self.assertEqual(search_term, sel.get_value(search_page_obj.search_box))
        
        search_term = "%25D"  
        search_page_obj.go_to_search_page()     
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        self.assertNotEqual("=", sel.get_value(search_page_obj.search_box))
        self.assertEqual(search_term, sel.get_value(search_page_obj.search_box))
        
        search_term = "&lsquo"  
        search_page_obj.go_to_search_page()     
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        self.assertNotEqual("'", sel.get_value(search_page_obj.search_box))
        self.assertEqual(search_term, sel.get_value(search_page_obj.search_box))