'''
Created on Aug 12, 2010

@author: mozilla
'''

import sumo_page
import vars

class OtherSupportPage(sumo_page.SumoPage):
    """    classdocs
    """
    
    title                    = 'Other Firefox support'
    page_url                 = '/kb/Other+Firefox+support'
    search_box               = "css=input[name='q']"
    search_button            = "css=input[type='submit']"
    moz_community_link       = "link=Mozilla Community"
    moz_zine_kb_link         = "link=MozillaZine Knowledge Base"
    moz_zine_forum_link      = "link=MozillaZine Firefox Support Forum"
    faq_link                 = "link=frequently asked support questions"
    win_bbs_link             = "link=Windows BBS Netscape and Mozilla Forum"
    netscape_faq_link        = "link=Netscape Unofficial FAQ Firefox Forums"
    silly_dog_link           = "css=a[href *= 'sillydog']"
    tbird_link               = "link=Thunderbird"
    moz_news_link            = "link=news.mozilla.org"
    alt_fan_text             = "*alt.fan.mozilla*"
    irc_link                 = "link=IRC"
    chatzilla_link           = "css=a[href *= 'http://www.irchelp.org/']"
    fx_channel_link          = "link=#firefox"
    
    
    def __init__(self,selenium):
        super(OtherSupportPage,self).__init__(selenium)
    
    def go_to_other_support_page(self):
        self.open(self.page_url)
        self.verify_page_title(self.title)
                          
    def do_search_on_search_box(self, search_query):
        self.type(self.search_box, search_query)
        self.click(self.search_button, True, vars.ConnectionParameters.page_load_timeout)
        
    def get_search_box_value(self):
        return self.selenium.get_value(self.search_box)
    