#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions as Exceptions
from selenium.webdriver.common.by import By

class Utils():

    def __init__(self, testsetup):
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

#    @property
    def find_element_and_wait(self,locator,parent=None):
     
        if parent is None:
            parent = self.selenium
        
        try:
            element = WebDriverWait(self.selenium,self.timeout). \
                                    until(lambda s: parent.find_element(*locator))        
        except Exceptions.TimeoutException:
            print "find_element_and_wait: failed to find the target element"
            element = None 
    
        return element

 #   @property
    def find_elements_and_wait(self,locator,parent=None):
        
        if parent is None:
            parent = self.selenium
        
        try:
            elements = WebDriverWait(self.selenium,self.timeout). \
                                     until(lambda s: parent.find_elements(*locator))
        except Exceptions.TimeoutException:
            print "find_elements_and_wait: failed to find the target element"
            elements = None
                
        return elements
    
    def match_urls(self, url1):
        
        current_addr = self.selenium.current_url
        if current_addr == url1:
            return True
        else:
            return False
        
    def go_back_page(self):
        
        self.selenium.back()