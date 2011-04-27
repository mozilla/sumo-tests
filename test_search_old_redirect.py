'''
Created on Aug 11, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import search_page


class OldSearchRedirect(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
        self.selenium.open(vars.ConnectionParameters.authurl)
        self.selenium.open(vars.ConnectionParameters.authurlssl)


    def tearDown(self):
        self.selenium.stop()

    def test_old_search_redirect(self):
        sel                = self.selenium
        search_page_obj    = search_page.SearchPage(sel)              
        search_word        = 'shockwave'
         
        """ check redirect from old tiki search """
        search_page_obj.open("/tiki-newsearch.php?where=all&locale=en-US&q=%s&sa=Search" %(search_word))

        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter+1
            else:
                not_found = False       
                
        self.failUnless("/search?" in sel.get_location(),"%s incorrect redirection" % sel.get_location())    
        self.failUnless(search_word in sel.get_location(), "No results for %s in %s" %(search_word,sel.get_location()))

        """ check redirect from old php search """
        search_page_obj.open("/search.php?q=%s&locale=en-US&where=all" %(search_word))

        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter+1
            else:
                not_found = False       
                
        self.failUnless("/search?" in sel.get_location(),"%s incorrect redirection" % sel.get_location())    
        self.failUnless(search_word in sel.get_location(), "No results for %s in %s" %(search_word,sel.get_location()))

if __name__ == "__main__":
    unittest.main()