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
Created on Aug 12, 2010

@author: mozilla
'''

import sumo_page
import vars

class OtherSupportPage(sumo_page.SumoPage):
    """    classdocs
    """
    
    _page_title              = 'Other Firefox support'
    page_url                 = '/kb/Other+Firefox+support'
    search_box               = "css=input[name='q']"
    search_button            = "css=input[type='submit']"
    moz_community_link       = "link=Mozilla Community"
    moz_zine_kb_link         = "link=MozillaZine Knowledge Base"
    moz_zine_forum_link      = "link=MozillaZine Firefox Support Forum"
    faq_link                 = "link=frequently asked support questions"
    win_bbs_link             = "link=Windows BBS Netscape and Mozilla Forum"
    netscape_faq_link        = "link=Netscape Unofficial FAQ Firefox Forums"
    silly_dog_link           = "css=a[href *= 'sillydog']"
    tbird_link               = "link=Thunderbird"
    moz_news_link            = "link=news.mozilla.org"
    alt_fan_text             = "*alt.fan.mozilla*"
    irc_link                 = "link=IRC"
    chatzilla_link           = "css=a[href *= 'http://www.irchelp.org/']"
    fx_channel_link          = "link=#firefox"
    
    
    def __init__(self,selenium):
        super(OtherSupportPage,self).__init__(selenium)
    
    def go_to_other_support_page(self):
        self.open(self.page_url)
        self.is_the_current_page
                          
    def do_search_on_search_box(self, search_query):
        self.type(self.search_box, search_query)
        self.click(self.search_button, True, vars.ConnectionParameters.page_load_timeout)
        
    def get_search_box_value(self):
        return self.selenium.get_value(self.search_box)
    