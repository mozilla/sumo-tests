#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Crash Tests Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

'''
Created on Jun 21, 2010

@author: mozilla
'''
import re
import time
import base64

class Page(object):
    '''
    Base class for all Pages
    '''

        
    def __init__(self, selenium):
        '''
        Constructor
        '''
        self.selenium = selenium
        
        
    def verify_page_title(self, title_regexp):
        if (re.search(title_regexp, self.selenium.get_title()) is None):
            raise Exception,'\r\nPage tile verification failed. Expected: %s; Actual:%s\r\n' %(title_regexp,self.selenium.get_title())
       
        
    def click_link(self, link, wait_flag=False,timeout=80000):
        self.selenium.click("link=%s" %(link))
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)
        
    def click(self,locator,wait_flag=False,timeout=80000):
        self.selenium.click(locator)
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)
            
    def type(self,locator, str):
        self.selenium.type(locator, str)
        
    def click_button(self,button,wait_flag=False,timeout=80000):
        self.selenium.click(button)
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)

    def get_url_current_page(self):
        return(self.selenium.get_location())
    
    def is_element_present(self,locator):
        return self.selenium.is_element_present(locator)
    
    def is_text_present(self,text):
        return self.selenium.is_text_present(text)
    
    def refresh(self,timeout=80000):
        self.selenium.refresh()
        self.selenium.wait_for_page_to_load(timeout)

    def record_error(self):
        '''

        '''
        print '-------------------'
        print 'Error at ' + self.selenium.get_location()
        print 'Page title ' + self.selenium.get_title()
        print '-------------------'
        filename = 'socorro_' + str(time.time()).split('.')[0] + '.png'

        print 'Screenshot of error in file ' + filename
        f = open(filename, 'wb')
        f.write(base64.decodestring(
            self.selenium.capture_entire_page_screenshot_to_string('')))
        f.close()
