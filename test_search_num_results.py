'''
Created on Aug 6, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import search_page

class SearchNumResults(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

    def test_search_num_results(self):
        sel = self.selenium
        search_page_obj       = search_page.SearchPage(sel)
        
        search_page_obj.go_to_search_page()
                
        search_terms = ["crashes", "firefox crashes"]
        for current_search_term in search_terms:
            search_page_obj.do_search_on_search_box(current_search_term)
            not_found = True
            counter = 0
            while(not_found and counter < 3):
                if(not(search_page_obj.is_search_available())):
                    search_page_obj.refresh()
                    counter = counter+1
                else:
                    not_found = False
            """ 
            Verify that there are 10 results on the page
            After that, click the "Next" link,
            until we're at the end of the search results:
            """
                     
            counter = 1
            while ( search_page_obj.is_element_present(search_page_obj.next_page_link) and counter < 11 ):
                self.failUnless(search_page_obj.are_ten_results_present(), "Ten results not present for %s" %(current_search_term))
                search_page_obj.click(search_page_obj.next_page_link, True)

                # Verify that we have a Next link on this page, otherwise,
                # we're at the end of the results and don't need to
                # count the results anymore!
                counter += 1
        
 

if __name__ == "__main__":
    unittest.main()