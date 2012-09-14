#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class SearchPage(Base):
    """
    'Search for Firefox Help' page
    """

    _page_title = 'Search | Mozilla Support'
    _page_url = '/en-US/search'
    _search_query_locator = (By.CSS_SELECTOR, 'input.search-query')
    _search_box_locator = (By.CSS_SELECTOR, 'input.searchbox')
    _search_button = (By.CSS_SELECTOR, 'input[type="submit"]')
    _search_support_button_locator = (By.CSS_SELECTOR, 'form.search-form > button.btn')
    _refine_search_link = (By.CSS_SELECTOR, 'a[href *= "a=2"]')
    _next_page_link = (By.LINK_TEXT, 'Next')
    _prev_page_link = (By.LINK_TEXT, 'Previous')
    _result_div = (By.CSS_SELECTOR, 'div.result')
    _second_page_link = (By.LINK_TEXT, '2')
    _search_unavailable_msg = 'unavailable'
    _results_list_locator = (By.CSS_SELECTOR, 'div.search-results div[class*="result"]')

    def do_search_on_search_query(self, search_query):
        if not (self._page_title in self.selenium.title):
            self.go_to_search_page()
        self.selenium.find_element(*self._search_query_locator).send_keys(search_query)
        self.selenium.find_element(*self._search_button).click()
    
    def do_search_on_search_box(self, search_term):
        if not (self._page_title in self.selenium.title):
            self.go_to_search_page()
        self.selenium.find_element(*self._search_box_locator).send_keys(search_term)
        self.selenium.find_element(*self._search_support_button_locator).click()

    def get_search_box_value(self):
        return self.selenium.find_element(*self._search_box).value

    @property
    def is_result_present(self):
        return self.is_element_present(*self._result_div)

    @property
    def are_ten_results_present(self):
        return len(self.selenium.find_elements(*self._results_list_locator)) == 10

    @property
    def get_result_text(self):
        return self.selenium.find_element(*self._result_div).text

    def click_refine_search_link(self, refine_search_page_obj):
        self.selenium.find_element(*self._refine_search_link).click()
        refine_search_page_obj.is_the_current_page

    def click_next_page_link(self):
        self.selenium.find_element(*self._next_page_link).click()
