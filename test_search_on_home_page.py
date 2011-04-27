'''
Created on Jun 25, 2010

@author: mozilla
'''
from selenium import selenium
import vars
import unittest

import support_home_page
import search_page

class SearchOnHomePage(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)


    def tearDown(self):
        self.selenium.stop()


    def test_search_on_home_page(self):
        sel = self.selenium
        support_home_page_obj = support_home_page.SupportHomePage(sel)
        search_page_obj       = search_page.SearchPage(sel)
                 
        search_term = 'iphone'
        support_home_page_obj.go_to_support_home_page()
        support_home_page_obj.do_search_on_main_search_box(search_term,search_page_obj)

        url = search_page_obj.get_url_current_page()
        self.failUnless(search_term in url, "Search term %s does not exist in the url %s" %(search_term,url))
        
#    def test_search_advanced(self):
#        user_info       = sumo_test_data.SUMOtestData().getUserInfo(0)
#        uname           = user_info['username']
#        pwd             = user_info['password']
#                   
#        search_term = 'support'
#        sel         = self.selenium
#        
#        login_page_obj         = login_page.LoginPage(sel)
#        support_home_page_obj  = support_home_page.SupportHomePage(sel)
#        refine_search_page_obj = refine_search_page.RefineSearchPage(sel)
#        search_page_obj        = search_page.SearchPage(sel)
#        
#        login_page_obj.log_in(uname, pwd)
#        
#        support_home_page_obj.go_to_support_home_page()
#        support_home_page_obj.do_search_on_main_search_box(search_term, search_page_obj)
#        not_found = True
#        counter = 0
#        while(not_found and counter < 3):
#            if(not(search_page_obj.is_search_available())):
#                search_page_obj.refresh()
#                counter = counter + 1
#            else:
#                not_found = False
#        self.failUnless(search_page_obj.is_text_present(search_term),"search query not present")
#        
#        """ Advanced """
#        support_home_page_obj.go_to_support_home_page()
#        support_home_page_obj.click_advanced_search_link(refine_search_page_obj)
#        
#        refine_search_page_obj.do_search_on_knowledge_base(search_term, search_page_obj)
#        url = refine_search_page_obj.get_url_current_page()
#        self.failUnless(search_term in url, "Search term %s does not exist in the url %s" %(search_term,url))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()