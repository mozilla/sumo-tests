#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.mobile.base import Base


class Home(Base):

    _page_title = 'Firefox for Mobile Support Home Page | Firefox Help'

    _header_locator = (By.CSS_SELECTOR, 'h1.site-title > a')
    _search_box_locator = (By.NAME, 'q')
    _search_button_locator = (By.CSS_SELECTOR, 'form#search > button')

    def __init__(self, testsetup):
        Base.__init__(self, testsetup)
        self.selenium.get(self.base_url)

    @property
    def header_text(self):
        return self.selenium.find_element(*self._header_locator).text

    @property
    def header_title(self):
        return self.selenium.find_element(*self._header_locator).get_attribute('title')

    def search_for(self, search_term, click_button=True):
        search_box = self.selenium.find_element(*self._search_box_locator)
        search_box.send_keys(search_term)

        if click_button:
            self.selenium.find_element(*self._search_button_locator).click()
        else:
            search_box.submit()

        from pages.mobile.search import Search
        return Search(self.testsetup, search_term)
