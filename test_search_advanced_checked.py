'''
Created on Aug 6, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import search_page
import refine_search_page


class AdvancedSearchChecked(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        print self.selenium
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

    def test_advanced_search_checked(self):
        sel = self.selenium
        refine_search_page_obj     = refine_search_page.RefineSearchPage(sel) 
        search_page_obj            = search_page.SearchPage(sel)
        
        refine_search_page_obj.go_to_refine_search_page()
        self.failUnless(refine_search_page_obj.is_kb_cat_checked(), "Default search forum is not set to Firefox")
        
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
        search_page_obj.verify_page_title(search_page_obj.title)

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
        search_page_obj.verify_page_title(search_page_obj.title)

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
        search_page_obj.verify_page_title(search_page_obj.title)
if __name__ == "__main__":
    unittest.main()