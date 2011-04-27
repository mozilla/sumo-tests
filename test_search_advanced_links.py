'''
Created on Aug 6, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import search_page
import refine_search_page
import support_home_page

class AdvancedSearchLinks(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

    def test_search_advanced_links(self):
        sel = self.selenium
        search_page_obj             = search_page.SearchPage(sel)
        refine_search_page_obj     = refine_search_page.RefineSearchPage(sel) 
        support_home_page_obj      = support_home_page.SupportHomePage(sel)

        support_home_page_obj.go_to_support_home_page()
        support_home_page_obj.do_search_on_main_search_box("dfg", search_page_obj)
        search_page_obj.click_refine_search_link(refine_search_page_obj)
        self.failUnless("a=2" in refine_search_page_obj.get_url_current_page(),
                        "%s not in URL: %s" % ("a=2", sel.get_location()))   
 

if __name__ == "__main__":
    unittest.main()