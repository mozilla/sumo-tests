'''
Created on Aug 6, 2010

@author: mozilla
'''

import sumo_page
import vars

page_load_timeout = vars.ConnectionParameters.page_load_timeout

class SupportWebsiteForumsPage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    title                  = 'Support Website Forums'
    ask_question_link      = "css=div#mainpagecontainer > p > a[href *= '/questions/new']"
    advanced_search_link   = "css=a.home-advanced-search"
    page_url               = "/en-US/kb/Support+Website+Forums"
    
    def __init__(self,selenium):
        super(SupportWebsiteForumsPage,self).__init__(selenium)               
        
    def clik_advanced_search_link(self,refine_search_page_obj):
        self.click(self.advanced_search_link,True,page_load_timeout)
        refine_search_page_obj.verify_page_title(refine_search_page_obj.title)
                
    def go_to_support_websites_forum_page(self):
        self.open(self.page_url)