#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
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

    _log_out_link = "css=a[href *='logout']"
    _my_account_link = "css=a[href *='user_preferences']"
    _kb_link = "link=*Home*"
    _question_link = "link=*Question*"
    _login_link = "css=a[href *= 'login']"

    def log_out(self):
        self.click(self._log_out_link, True)

    def open(self, url, count=0):
        try:
            self.selenium.open(url)
            is_page_500 = re.search("500", self.selenium.get_title())
            is_page_error = re.search("Error", self.selenium.get_title(), re.IGNORECASE)
            is_page_problem = re.search("Problem", self.selenium.get_title(), re.IGNORECASE)
            is_search_unavail = self.selenium.is_text_present("Search Unavailable")
            if ((is_page_500 is not None or is_page_error is not None or is_page_problem is not None or is_search_unavail) and count < 10):
                    count = count + 1
                    self.open(url, count)
        except Exception, e:
            if count < 10:
                count = count + 1
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

    def click(self, locator, wait_flag=False, timeout=120000):
        count = 0
        try:
            self.selenium.click(locator)
            if(wait_flag):
                self.selenium.wait_for_page_to_load(timeout)
                is_page_500 = re.search("500", self.selenium.get_title())
                is_page_error = re.search("Error", self.selenium.get_title(), re.IGNORECASE)
                is_page_problem = re.search("Problem", self.selenium.get_title(), re.IGNORECASE)
                is_search_unavail = self.selenium.is_text_present("Search Unavailable")
                while((is_page_500 is not None or is_page_error is not None or is_page_problem is not None or is_search_unavail) and count < 10):
                        count = count + 1
                        self.refresh(timeout)
                        is_page_500 = re.search("500", self.selenium.get_title())
                        is_page_error = re.search("Error", self.selenium.get_title(), re.IGNORECASE)
                        is_page_problem = re.search("Problem", self.selenium.get_title(), re.IGNORECASE)
                        is_search_unavail = self.selenium.is_text_present("Search Unavailable")
        except Exception, e:
            if(wait_flag and count < 10):
                is_page_500 = re.search("500", self.selenium.get_title())
                is_page_error = re.search("Error", self.selenium.get_title(), re.IGNORECASE)
                is_page_problem = re.search("Problem", self.selenium.get_title(), re.IGNORECASE)
                is_search_unavail = self.selenium.is_text_present("Search Unavailable")
                while((is_page_500 is not None or is_page_error is not None or is_page_problem is not None or is_search_unavail) and count < 10):
                        count=count + 1
                        self.refresh(timeout)
                        is_page_500 = re.search("500", self.selenium.get_title())
                        is_page_error = re.search("Error", self.selenium.get_title(), re.IGNORECASE)
                        is_page_problem = re.search("Problem", self.selenium.get_title(), re.IGNORECASE)
                        is_search_unavail = self.selenium.is_text_present("Search Unavailable")
            else:
                print self.selenium.get_title()
                print e
                print "\n--------------------------\n"
                print self.selenium.get_html_source()
                print "\n--------------------------\n"
                sys.exit(0)
