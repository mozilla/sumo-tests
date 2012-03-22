#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.mobile.base import Base


class Home(Base):

    _page_title = 'Firefox for Mobile Support Home Page | Firefox Help'

    _header_locator = (By.CSS_SELECTOR, 'h1.site-title > a')

    def __init__(self, testsetup):
        Base.__init__(self, testsetup)
        self.selenium.get(self.base_url)

    @property
    def header_text(self):
        return self.selenium.find_element(*self._header_locator).text

    @property
    def header_title(self):
        return self.selenium.find_element(*self._header_locator).get_attribute('title')
