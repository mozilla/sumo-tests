'''
Created on Jul 27, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import search_page

class NonNumericSearchPages(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

    def test_nonnumeric_search_pages(self):
        sel = self.selenium
        search_page_obj       = search_page.SearchPage(sel)
                
        url = "/en-US/search?q=firefox+crashes&page="
        pages = ["string", "2str", "$@&%*", "?2"]
        for page in pages:
            search_page_obj.open(url+page)
            not_found = True
            counter = 0
            while(not_found and counter < 3):
                if(not(search_page_obj.is_search_available())):
                    search_page_obj.refresh()
                    counter = counter+1
                else:
                    not_found = False
            self.failUnless(search_page_obj.is_element_present(search_page_obj.result_div), "No search results for non-numeric pages")
        
        
 

if __name__ == "__main__":
    unittest.main()