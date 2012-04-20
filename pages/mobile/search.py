#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.mobile.base import Base
from pages.page import Page


class Search(Base):

    _page_url = '/en-US/search'
    _results_locator = (By.CSS_SELECTOR, 'ol.search-results li')

    def __init__(self, testsetup, search_term):
        Base.__init__(self, testsetup)
        self._page_title = "%s :: Search :: Add-ons for Firefox" % search_term

    @property
    def results(self):
        return [self.SearchResult(self.testsetup, web_element)
                for web_element in self.selenium.find_elements(*self._results_locator)]

    class SearchResult(Page):
        def __init__(self, testsetup, web_element):
            Page.__init__(self, testsetup)
            self._root_element = web_element
