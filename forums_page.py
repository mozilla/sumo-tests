'''
Created on Jul 15, 2010

@author: mozilla
'''
import sumo_page
import vars

pageLoadTimeout = vars.ConnectionParameters.page_load_timeout

class ForumsPage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    title                  = 'Forums'
    forums_cat_list_url    = vars.ConnectionParameters.baseurl_ssl+'/en-US/forums'
    kb_articles_forum_url  = vars.ConnectionParameters.baseurl_ssl+'/en-US/forums/knowledge-base-articles'
    first_cat_forum_link   = "css=div.name > a"
    post_new_thread_link   = "new-thread"
    thread_title_box       = "css=input#id_title"
    thread_content_box     = "id_content"
    post_button            = "css=input[value='Post']"
    cancel_link            = "link=Cancel"
    reply_button           = "css=input[value='Reply']"
    reply_link             = "css=a[href *= 'reply']"
    pagination_link        = "css=ol.pagination"
    next_page_link         = "css=li.next"
    prev_page_link         = "css=li.prev"
    locked_thread_format   = "css=ol.threads li:nth-child(%d) > div > img[title='Locked']"
    unlocked_thread_format = "css=ol.threads > li:nth-child(%d) > div:nth-child(2) > a"
    
    def __init__(self,selenium):
        super(ForumsPage,self).__init__(selenium)               
        
    def post_new_thread_first_cat(self, thread_title,thread_content):
        self.click(self.post_new_thread_link,True,pageLoadTimeout)
        self.selenium.type(self.thread_title_box, thread_title)
        self.selenium.type(self.thread_content_box, thread_content)
        self.click(self.post_button,True,pageLoadTimeout)
        if(not (self.selenium.is_text_present(thread_title))):
            raise Exception("Posting new thread failed\r\n")
    
    def go_to_forums_cat_list_page(self):
        self.open(self.forums_cat_list_url)
        self.verify_page_title(self.title)
        
    def post_reply(self,thread_url,reply_text):
        self.go_to_thread(thread_url)
        self.selenium.type(self.thread_content_box,reply_text)
        self.click(self.reply_button,True,pageLoadTimeout)
        if(not(self.selenium.is_text_present(reply_text))):
            raise Exception('Posting reply failed\r\n')
        
    def go_to_thread(self,url):
        self.open(url)
        
