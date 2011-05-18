'''
Created on Aug 6, 2010

@author: mozilla
'''

import pytest

import search_page
import refine_search_page

@pytest.mark.smoketests
class TestAdvancedSearchChecked:

    def test_advanced_search_checked(self, testsetup):
        refine_search_page_obj     = refine_search_page.RefineSearchPage(testsetup) 
        search_page_obj            = search_page.SearchPage(testsetup)
        
        refine_search_page_obj.go_to_refine_search_page()
        assert(refine_search_page_obj.is_kb_cat_checked(), "Default search forum is not set to Firefox")
        
        search_word = 'firefox crashes' 
        """ search kb tab """
        refine_search_page_obj.do_search_on_knowledge_base(search_word, search_page_obj)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter+1
            else:
                not_found = False           
        search_page_obj.is_the_current_page

        """ search support questions tab """
        refine_search_page_obj.go_to_refine_search_page()
        refine_search_page_obj.do_search_on_support_questions(search_word, search_page_obj)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter+1
            else:
                not_found = False           
        search_page_obj.is_the_current_page

        """ search discussion forums tab """
        refine_search_page_obj.go_to_refine_search_page()
        refine_search_page_obj.do_search_on_discussion_forums(search_word, search_page_obj)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter+1
            else:
                not_found = False           
        search_page_obj.is_the_current_page