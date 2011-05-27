'''
Created on Jun 30, 2010

@author: mozilla
'''
import sumo_page
import vars

class LoginPage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    title           = 'Log In'
    page_url        = '/en-US/users/login'
    username_box    = 'id_username'
    password_box    = 'id_password'
    log_in_button   = "css=input[type='submit']"
    log_in_link     = "css=a[href *= 'login']"
    log_out_link    = "css=a[href *= 'logout']"
    
    """ if user is logged-in then you see these elements"""
    logged_in_as_div = "css=div#mod-login_box > div"
    logged_in_text   = "Logged in as"
    
    def __init__(self,selenium):
        super(LoginPage,self).__init__(selenium)   
     
    def go_to_login_page(self):
        self.open(self.page_url)
        self.verify_page_title(self.title)   
        
    def log_in(self, uname,pwd):
        if(not (self.title in self.selenium.get_title())):
            self.go_to_login_page()
        
        self.type(self.username_box,uname)
        self.type(self.password_box, pwd)
        self.click_button(self.log_in_button)
        self.selenium.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        if(not (self.selenium.is_element_present(self.log_out_link))):
            raise Exception, 'Login Failed\r\n'
    
    
    """ if user is logged out then you see these elements"""
    logged_out_text  = "Want to contribute?"
    
    def log_out(self):
        self.click_button(self.log_out_link)
        self.selenium.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
        if(not (self.selenium.is_element_present(self.log_in_link))):
            raise Exception, 'Logout Failed\r\n'
