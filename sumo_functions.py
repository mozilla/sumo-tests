'''
Created on May 17, 2010

@author: mozilla
'''
import sumo_test_data
import vars
import sys
import urllib
import time

class SUMOfunctions(object):
    '''
    all functions that will be used by SUMO app.
    '''
    pageLoadTimeout = vars.ConnectionParameters.page_load_timeout
    
    def __init__(self):
        '''
        Constructor
        '''
        self.objTestData = sumo_test_data.SUMOtestData()
        
    def login(self,userType,sel):
        user = self.objTestData.getUserInfo(userType)
        self.open(sel, "/en-US/users/login")
        if(sel.is_element_present('link=Sign Out')):
            sel.click('link=Sign Out')
            sel.wait_for_page_to_load(SUMOfunctions.pageLoadTimeout)
            self.open(sel, "/en-US/users/login")
            
        sel.type("id_username", user['username'])
        sel.type("id_password", user['password'])
        sel.click("css=input[type='submit']")
        sel.wait_for_page_to_load(SUMOfunctions.pageLoadTimeout)
        if(sel.is_element_present('link=Sign Out')):
            return True
        else:
            raise Exception, "Login Failed"
            return False

    def logout(self,sel):
        if(sel.is_element_present('link=Sign Out')):
            sel.click('link=Sign Out')
            sel.wait_for_page_to_load(SUMOfunctions.pageLoadTimeout)
            if(not(sel.is_element_present('link=Sign Out'))):
                return True
            else:
                raise Exception, "Logout failed"
                return False
        else:
            pass

    def getResponse(self,url):
        conn = urllib.urlopen(url)
        status = conn.getcode()
        return status
        
    def open(self,sel,url,count=0):
        try:
            sel.open(url)
        except Exception, e:
            if count < 10:
                count = count+1
                self.open(sel, url, count)
                time.sleep(2)
            else:
                if sel.is_text_present("Search Unavailable"):
                    print "Search unavailable"
                print e
                print "\n--------------------------\n"
                print sel.get_html_source()
                print "\n--------------------------\n"
                sys.exit(0)
            
            