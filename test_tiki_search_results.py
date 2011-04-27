'''
Created on Jul 26, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import support_home_page
import search_page

class TikiSearchResult(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

    def test_tiki_search_result(self):
        sel = self.selenium
        support_home_page_obj = support_home_page.SupportHomePage(sel)
        search_page_obj       = search_page.SearchPage(sel)
                
        search_term = 'firefox crashes'
        support_home_page_obj.go_to_support_home_page()
        support_home_page_obj.do_search_on_main_search_box(search_term,search_page_obj)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_element_present(search_page_obj.second_page_link))):
                sel.refresh()
                sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                counter = counter+1
            else:
                not_found = False

        self.failUnless(search_page_obj.is_element_present((search_page_obj.second_page_link)))
        self.failUnless(search_page_obj.is_element_present((search_page_obj.next_page_link)))
        self.assertEqual(search_term, search_page_obj.get_search_box_value())
        self.failUnless(search_page_obj.is_element_present(
            search_page_obj.result_div),
            "Result not present")
        self.failUnless(search_page_obj.is_element_present(
            search_page_obj.support_question_link))
        self.failUnless(search_page_obj.is_element_present(search_page_obj.kb_link))
        self.failUnless(search_page_obj.is_element_present(search_page_obj.question_link))
        
 

if __name__ == "__main__":
    unittest.main()