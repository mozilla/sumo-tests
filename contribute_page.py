'''
Created on Aug 11, 2010

@author: mozilla
'''

import sumo_page
import vars

pageLoadTimeout = vars.ConnectionParameters.page_load_timeout

class ContributePage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    title                  = 'How to contribute'
    page_url               = '/en-US/kb/How+to+contribute'
    
    improve_kb_link        = "css=a[href *= 'Contributing+to+the+Knowledge+Base']"
    translate_link         = "css=a[href *= 'Translating+articles']"
    forum_support_link     = "css=a[href *= 'Providing+Forum+Support']"
    live_chat_link         = "css=a[href *= 'Helping+with+Live+Chat']"
    stay_in_contact_link   = "css=a[href *= 'Stay_connected']"
    
    
    def __init__(self,selenium):
        super(ContributePage,self).__init__(selenium)               
           
    def go_to_contribute_page(self):
        self.open(self.page_url)
        self.verify_page_title(self.title)
        

        
