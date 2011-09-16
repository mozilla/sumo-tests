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
# Mozilla
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
from page import Page

import sys
import time
import re


class SumoPage(Page):
    """
     SumoPage contains common web elements found across
     all SUMO pages. Every new SUMO page class is derived from
     SumoPage so that every child class can have access to common web 
     elements and methods that pertain to those elements.
    """
 
    log_out_link = "css=a[href *='logout']"
    my_account_link = "css=a[href *='user_preferences']"
    kb_link = "link=*Home*"
    question_link = "link=*Question*"
    login_link = "css=a[href *= 'login']"

    def log_out(self):
        self.click(self.log_out_link, True)
        
    def open(self,url,count=0):
        try:
            self.selenium.open(url)
            is_page_500 = re.search("500", self.selenium.get_title())
            is_page_error = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
            is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
            is_search_unavail = self.selenium.is_text_present("Search Unavailable")
            if ((is_page_500 is not None or is_page_error is not None or is_page_problem is not None or is_search_unavail) and count < 10):
                    count=count+1
                    self.open(url, count)
        except Exception, e:
            if count < 10:
                count = count+1
                self.open(url, count)
                time.sleep(2)
            else:
                if self.is_text_present("Search Unavailable") or self.is_text_present("Service Unavailable"):
                    print "Search/Service unavailable"
                print e
                print "\n--------------------------\n"
                print self.selenium.get_html_source()
                print "\n--------------------------\n"
                sys.exit(0)
                
    def click(self,locator,wait_flag=False,timeout=120000):
        count=0
        try:
            self.selenium.click(locator)
            if(wait_flag):
                self.selenium.wait_for_page_to_load(timeout)
                is_page_500 = re.search("500", self.selenium.get_title())
                is_page_error = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
                is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
                is_search_unavail = self.selenium.is_text_present("Search Unavailable")
                while((is_page_500 is not None or is_page_error is not None or is_page_problem is not None or is_search_unavail) and count < 10):
                        count=count+1
                        self.refresh(timeout)
                        is_page_500     = re.search("500", self.selenium.get_title())
                        is_page_error   = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
                        is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
                        is_search_unavail = self.selenium.is_text_present("Search Unavailable")
        except Exception, e:
            if( wait_flag and count < 10):
                is_page_500 = re.search("500", self.selenium.get_title())
                is_page_error = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
                is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
                is_search_unavail = self.selenium.is_text_present("Search Unavailable")
                while((is_page_500 is not None or is_page_error is not None or is_page_problem is not None or is_search_unavail) and count < 10):
                        count=count+1
                        self.refresh(timeout)
                        is_page_500     = re.search("500", self.selenium.get_title())
                        is_page_error   = re.search("Error", self.selenium.get_title(),re.IGNORECASE)
                        is_page_problem = re.search("Problem", self.selenium.get_title(),re.IGNORECASE)
                        is_search_unavail = self.selenium.is_text_present("Search Unavailable")
            else:
                print self.selenium.get_title()
                print e
                print "\n--------------------------\n"
                print self.selenium.get_html_source()
                print "\n--------------------------\n"
                sys.exit(0)