'''
Created on Jun 30, 2010

@author: mozilla
'''
import sumo_page
import vars

class RefineSearchPage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    title = 'Search'
    page_url = '/en-US/search?a=2'
    article_search_box = "kb_q"
    post_search_box    = 'support_q'
    post_tags_box      = 'id_q_tags'
    thread_search_box  = 'discussion_q'
    search_button_kb      = "css=input[name='w'][value='1']+div.submit-search > input[type='submit']"
    search_button_support = "css=input[name='w'][value='2']+div.submit-search > input[type='submit']"
    search_button_disc    = "css=input[name='w'][value='4']+div.submit-search > input[type='submit']"
    kb_cat_check_box = "css=input#id_category_0"
    kb_tab                = "css=div#search-tabs > ul > li:nth-child(1) > a"
    support_questions_tab = "css=div#search-tabs > ul > li:nth-child(2) > a"
    forums_tab            = "css=div#search-tabs > ul > li:nth-child(3) > a"
    
    
    def __init__(self,selenium):
        super(RefineSearchPage,self).__init__(selenium)               
    
    def go_to_refine_search_page(self):
        self.open(self.page_url)
        self.verify_page_title(self.title)
        
    def do_search_on_knowledge_base(self, search_query,search_page_obj):
        self.click(self.kb_tab)
        self.type(self.article_search_box, search_query)
        self.click(self.search_button_kb,True)
        search_page_obj.verify_page_title(search_page_obj.title)
        
    def do_search_on_support_questions(self, search_query,search_page_obj):
        self.click(self.support_questions_tab)
        self.type(self.post_search_box, search_query)
        self.click(self.search_button_support,True)
        search_page_obj.verify_page_title(search_page_obj.title)
        
    def do_search_tags_on_support_questions(self, search_query,search_page_obj):
        self.click(self.support_questions_tab)
        self.type(self.post_tags_box, search_query)
        self.click(self.search_button_support,True)
        search_page_obj.verify_page_title(search_page_obj.title)
        
    def do_search_on_discussion_forums(self, search_query,search_page_obj):
        self.click(self.forums_tab)
        self.type(self.thread_search_box, search_query)
        self.click(self.search_button_disc,True)
        search_page_obj.verify_page_title(search_page_obj.title)
        
    def is_kb_cat_checked(self):
        return self.selenium.is_checked(self.kb_cat_check_box)