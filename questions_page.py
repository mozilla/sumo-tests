'''
Created on Aug 10, 2010

@author: mozilla
'''

import sumo_page
import vars
import time


page_load_timeout = vars.ConnectionParameters.page_load_timeout

class QuestionsPage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    title_forums                  = 'Firefox Support Forum'
    title_questions_new           = 'Ask a Question'
    forums_page_url               = '/en-US/questions'
    questions_new_url             = '/en-US/questions/new'
    ask_question_link             = '/en-US/questions/new'
    firefox_product_first_link    = 'css=ul.select-one > li > a'
    category_prob_first_link      = 'css=ul.select-one > li > a'
    type_question_box             = 'search'
    ask_this_button               = "css=input[value='Ask this']"
    none_of_these_button          = "css=input[value *='None']"
    question_list_link            = "css=ol.questions > li:nth-child(%d) > div:nth-child(1) > h2 > a"
    problem_too_button            = "css=input[value*='problem']"
    no_thanks_link                = "link=*No*Thanks*"
    problem_count_text            = "css=div[class^='have-problem'] > mark"
    
    def __init__(self,selenium):
        super(QuestionsPage,self).__init__(selenium)               
        
    
    def go_to_forum_questions_page(self):
        self.open(self.forums_page_url)
        self.verify_page_title(self.title_forums)
        
    def go_to_ask_new_questions_page(self):
        self.selenium.open(self.questions_new_url)
        self.verify_page_title(self.title_questions_new)
    
    def click_ask_new_questions_link(self):
        self.click(self.ask_question_link, True, page_load_timeout)
        
    def click_firefox_product_link(self):
        self.click(self.firefox_product_first_link, True, page_load_timeout)
        
    def click_category_problem_link(self):
        self.click(self.category_prob_first_link, True, page_load_timeout)
        
    def type_question(self, question_to_ask):
        self.type(self.type_question_box, question_to_ask)
          
    def go_to_thread(self,url):
        self.selenium.open(url)
        
    def click_any_question(self,num):
        q_link = self.question_list_link %(num)
        self.selenium.click(q_link)
        self.selenium.wait_for_page_to_load(page_load_timeout)
        
    def click_problem_too_button(self):
        self.selenium.click(self.problem_too_button)
        time.sleep(2)
        #self.selenium.click(self.no_thanks_link)
        
    def get_problem_count(self):
        count_text = self.selenium.get_text(self.problem_count_text)
        count_text = count_text.split()
        count = int(count_text[0])
        return count
        
        
        
    
        
