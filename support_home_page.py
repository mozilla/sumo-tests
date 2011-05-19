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
# The Original Code is Mozilla Support
#
# The Initial Developer of the Original Code is
# Mozilla Support
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
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

import sumo_page

class SupportHomePage(sumo_page.SumoPage):
    """
    The Firefox Support Home Pgae contains 
    web elements and methods that can be 
    performed on them.
    """
    _page_title             = 'Firefox Support Home Page'
    main_search_box         = 'q'
    log_in_link             = 'log in'
    search_button           = 'css=button.img-submit'
    see_all_button          = "button-seeall"
    
    
    def __init__(self,testsetup):
        super(SupportHomePage,self).__init__(testsetup)
    
    def go_to_support_home_page(self):
        self.open('/')
        self.is_the_current_page
                   
    def click_log_in_link(self):
        self.click(self.log_in_link,True,self.timeout)
        
    def do_search_on_main_search_box(self, search_query, search_page_obj):
        if(re.search(self._page_title, self.selenium.get_title()) is None):
            self.go_to_support_home_page()
        self.type(SupportHomePage.main_search_box, search_query)
        self.click(self.search_button,True,self.timeout)
        count = 0
        while not self.selenium.is_text_present('results for ' + search_query):
            time.sleep(1)
            count += 1
            if count == self.timeout/1000:
                self.record_error()
                raise Exception(search_query + " search page hasnt loaded")
        search_page_obj.is_the_current_page
