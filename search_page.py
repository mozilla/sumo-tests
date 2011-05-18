'''
Created on Jun 25, 2010

@author: mozilla
'''
import sumo_page

class SearchPage(sumo_page.SumoPage):
    """    classdocs
    """
    
    title                    = 'Search'
    page_url                 = 'en-US/search'
    search_box               = "css=input[name='q']"
    search_button            = "css=input[type='submit']"
    refine_search_link       = "css=a[href *= 'a=2']"
    next_page_link           = "link=*Next*"
    prev_page_link           = "link=*Previous*"
    result_div               = "css=div.result"
    support_question_link    = "link=*support*question*"
    second_page_link         = "link=2"
    search_unavailable_msg   = "unavailable"
    ten_search_results       = "css=div.search-results div[class*='result']:nth-child(10)"
    eleven_search_results    = "css=div.search-results div[class*='result']:nth-child(11)"
    
    def __init__(self,testsetup):
        super(SearchPage,self).__init__(testsetup)
    
    def go_to_search_page(self):
        self.open(self.page_url)
        self.verify_page_title(self.title)
                          
    def do_search_on_search_box(self, search_query):
        if(not (self.title in self.selenium.get_title())):
            self.go_to_search_page()
        count=1
        while(count < 5 and not(self.selenium.is_element_present(self.search_box))):
            self.go_to_search_page()
            count = count+1
        self.type(self.search_box, search_query)
        self.click(self.search_button,True,self.timeout)
        
        
    def get_search_box_value(self):
        return self.selenium.get_value(self.search_box)
    
    def is_search_available(self):
        if(self.is_text_present(self.search_unavailable_msg)):
            return False
        else:
            return True
    
    def is_result_present(self):
        return self.is_element_present(self.result_div)
      
    def are_ten_results_present(self):
        return self.is_element_present(self.ten_search_results) and not self.is_element_present(self.eleven_search_results)
    
    def click_refine_search_link(self,refine_search_page_obj):
        self.click(self.refine_search_link, True, self.timeout)
        refine_search_page_obj.verify_page_title(self.title)