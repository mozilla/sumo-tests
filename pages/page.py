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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

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
        if self._page_title:
            WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)

        if re.search(self._page_title, self.selenium.title) is None:
            raise Exception("Expected page title to be: '" + self._page_title + "' but it was: '" + actual_title + "'")
        else:
            return True

    @property
    def url_current_page(self):
        return(self.selenium.current_url)

    @property
    def page_title(self):
        return self.selenium.title()

    def refresh(self):
        self.selenium.refresh()
        #self.selenium.get(self.selenium.current_url)

    def open(self, url_fragment):
        self.selenium.get(self.base_url + url_fragment)
        
    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            # this will return a snapshot, which takes time.
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)
            
    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except NoSuchElementException, ElementNotVisibleException:
            # this will return a snapshot, which takes time.
            return False

    def wait_for_element_present(self, *locator):
        count = 0
        while not self.is_element_present(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(*locator + ' has not loaded')

    def wait_for_element_not_present(self, *locator):
        count = 0
        while self.is_element_present(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(*locator + ' is still present')
            
    def wait_for_element_visible(self, *locator):
        count = 0
        while not self.is_element_visible(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(*locator + " is not visible")

    def wait_for_element_not_visible(self, *locator):
        count = 0
        while self.is_element_visible(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                raise Exception(*locator + " is still visible")

    def wait_for_element_come_and_go(self, *locator):
        self.wait_for_element_present(*locator)
        self.wait_for_element_not_present(*locator)
        
    def get_user_name(self, user="default"):
        credentials = self.testsetup.credentials[user]
        return credentials['name']
