#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

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
        actual_title = self.selenium.get_title()
        if re.search(self._page_title, actual_title) is None:
            raise Exception("Expected page title to be: '" + self._page_title + "' but it was: '" + actual_title + "'")
        else:
            return True

    @property
    def url_current_page(self):
        return(self.selenium.get_location())

    @property
    def page_title(self):
        return self.selenium.get_title()

    def refresh(self):
        self.selenium.refresh()
        self.selenium.wait_for_page_to_load(self.timeout)

    def wait_for_element_present(self, locator):
        count = 0
        while not self.selenium.is_element_present(locator):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(locator + ' has not loaded')

    def wait_for_element_visible(self, locator):
        self.wait_for_element_present(locator)
        count = 0
        while not self.selenium.is_visible(locator):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(locator + " is not visible")

    def wait_for_element_not_visible(self, locator):
        count = 0
        while self.selenium.is_visible(locator):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(locator + " is still visible")
