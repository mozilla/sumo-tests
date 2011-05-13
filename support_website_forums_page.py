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
# Portions created by the Initial Developer are Copyright (C) 2___
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
Created on Aug 6, 2010

@author: mozilla
'''

import sumo_page
import vars

page_load_timeout = vars.ConnectionParameters.page_load_timeout

class SupportWebsiteForumsPage(sumo_page.SumoPage):
    '''
    classdocs
    '''
    _page_title            = 'Support Website Forums'
    ask_question_link      = "css=div#mainpagecontainer > p > a[href *= '/questions/new']"
    advanced_search_link   = "css=a.home-advanced-search"
    page_url               = "/en-US/kb/Support+Website+Forums"
    
    def __init__(self,selenium):
        super(SupportWebsiteForumsPage,self).__init__(selenium)               
        
    def clik_advanced_search_link(self,refine_search_page_obj):
        self.click(self.advanced_search_link,True,page_load_timeout)
        refine_search_page_obj.is_the_current_page
                
    def go_to_support_websites_forum_page(self):
        self.open(self.page_url)
        self.is_the_current_page