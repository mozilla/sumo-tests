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
Created on Jun 25, 2010

@author: mozilla
'''
import sumo_page

class SearchPage(sumo_page.SumoPage):
    """    
    'Search for Firefox Help' page
    """

    _page_title              = 'Search'
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
        self.is_the_current_page
               
    def do_search_on_search_box(self, search_query):
        if not (self._page_title in self.selenium.get_title()):
            self.go_to_search_page()
        count=1
        while count < 5 and not(self.selenium.is_element_present(self.search_box)):
            self.go_to_search_page()
            count = count+1
        self.type(self.search_box, search_query)
        self.click(self.search_button,True,self.timeout)

    def get_search_box_value(self):
        return self.selenium.get_value(self.search_box)

    def is_search_available(self):
        if self.is_text_present(self.search_unavailable_msg):
            return False
        else:
            return True

    def is_result_present(self):
        return self.is_element_present(self.result_div)

    def are_ten_results_present(self):
        return self.is_element_present(self.ten_search_results) and not self.is_element_present(self.eleven_search_results)

    def click_refine_search_link(self,refine_search_page_obj):
        self.click(self.refine_search_link, True, self.timeout)
        refine_search_page_obj.is_the_current_page

