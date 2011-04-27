'''
Created on Jun 21, 2010

@author: mozilla
'''
import sumo_page
import vars
import re
import logging
import time

page_load_timeout = vars.ConnectionParameters.page_load_timeout

class SupportHomePage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    title                   = 'Firefox Support Home Page'
    main_search_box         = 'q'
    log_in_link             = 'log in'
    search_button           = 'css=button.img-submit'
    """ advanced search link does not exist on homepage anymore (SUMO 2.3)"""
    #advanced_search_link    = "css=a.home-advanced-search"
    see_all_button          = "button-seeall"
    
    
    def __init__(self,selenium):
        super(SupportHomePage,self).__init__(selenium)
    
    def go_to_support_home_page(self):
        self.open('/')
        self.verify_page_title(self.title)
                   
    def click_log_in_link(self):
        self.click(self.log_in_link,True,vars.ConnectionParameters.page_load_timeout)
        
    def click_advanced_search_link(self, refine_search_page_obj):
        self.click(self.advanced_search_link,True,vars.ConnectionParameters.page_load_timeout)
        refine_search_page_obj.verify_page_title(refine_search_page_obj.title)
        
    def do_search_on_main_search_box(self, search_query, search_page_obj):
        if(re.search(self.title, self.selenium.get_title()) is None):
            self.go_to_support_home_page()
        self.type(SupportHomePage.main_search_box, search_query)
        self.click(self.search_button,True,vars.ConnectionParameters.page_load_timeout)
        count = 0
        while not self.selenium.is_text_present('results for ' + search_query):
            time.sleep(1)
            count += 1
            if count == page_load_timeout/1000:
                self.record_error()
                raise Exception(search_query + " search page hasnt loaded")
        print self.selenium.get_title() + ' is the page title'
        search_page_obj.verify_page_title(search_page_obj.title)
