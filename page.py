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
# The Original Code is Mozilla Firefox Support.
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
#                 Dave Hunt <dhunt@mozilla.com>
#                 David Burns
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

'''
import re
import time
import base64

http_regex = re.compile('https?://((\w+\.)+\w+\.\w+)')


class Page(object):
    """
    Base class for all Pages
    """
      
    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.base_url_ssl = testsetup.base_url.replace("http://", "https://")
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    @property
    def is_the_current_page(self):
        page_title = self.selenium.get_title()
        if re.search(self._page_title, page_title) is None:
            try:
                raise Exception("Expected page title to be: '" + self._page_title + "' but it was: '" + page_title + "'")
            except Exception:
                raise Exception('Expected page title does not match actual page title.')
        else:
            return True

    def click_link(self, link, wait_flag=False, timeout=80000):
        self.selenium.click("link=%s" % (link))
        if wait_flag:
            self.selenium.wait_for_page_to_load(timeout)

    def click(self, locator, wait_flag=False, timeout=80000):
        self.selenium.click(locator)
        if(wait_flag):
            self.selenium.wait_for_page_to_load(timeout)

    def type(self, locator, str):
        self.selenium.type(locator, str)

    def click_button(self, button, wait_flag=False, timeout=80000):
        self.selenium.click(button)
        if wait_flag:
            self.selenium.wait_for_page_to_load(timeout)

    def get_attribute(self, attributelocator):
        return self.selenium.get_attribute(attributelocator)

    def get_url_current_page(self):
        return(self.selenium.get_location())

    def get_page_title(self):
        return self.selenium.get_title()
        
    def get_text(self, locator):
        return self.selenium.get_text(locator)

    def is_element_present(self, locator):
        return self.selenium.is_element_present(locator)

    def is_element_visible(self, locator):
        return self.selenium.is_visible(locator)

    def is_text_present(self, text):
        return self.selenium.is_text_present(text)

    def refresh(self, timeout=80000):
        self.selenium.refresh()
        self.selenium.wait_for_page_to_load(timeout)

    def wait_for_element_present(self, element):
        count = 0
        while not self.is_element_present(element):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(element + ' has not loaded')

    def wait_for_element_visible(self, element):
        self.wait_for_element_present(element)
        count = 0
        while not self.is_element_visible(element):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(element + " is not visible")

    def wait_for_element_not_visible(self, element):
        count = 0
        while self.is_element_visible(element):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(element + " is still visible")

    def wait_for_page(self, url_regex):
        count = 0
        while (re.search(url_regex, self.selenium.get_location(), re.IGNORECASE)) is None:
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception("Sites Page has not loaded")