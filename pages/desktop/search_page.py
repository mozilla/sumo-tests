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

    _page_title = 'Advanced Search | Firefox Help'
    _page_url = '/en-US/search'
    _search_box = (By.CSS_SELECTOR, 'input.search-query')
    _search_button = (By.CSS_SELECTOR, 'input[type="submit"]')
    _refine_search_link = (By.CSS_SELECTOR, 'a[href *= "a=2"]')
    _next_page_link = (By.LINK_TEXT, 'Next')
    _prev_page_link = (By.LINK_TEXT, 'Previous')
    _result_div = (By.CSS_SELECTOR, 'div.result')
    _ask_a_question_locator = (By.CSS_SELECTOR, 'p.aaq')
    _support_question_link = (By.CSS_SELECTOR, 'p.aaq > a')
    _second_page_link = (By.LINK_TEXT, '2')
    _search_unavailable_msg = 'unavailable'
    _results_list_locator = (By.CSS_SELECTOR, 'div.search-results div[class*="result"]')

    def do_search_on_search_box(self, search_query):
        if not (self._page_title in self.selenium.title):
            self.go_to_search_page()
        self.selenium.find_element(*self._search_box).send_keys(search_query)
        self.selenium.find_element(*self._search_button).click()

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

    @property
    def ask_a_question_text(self):
        return self.selenium.find_element(*self._ask_a_question_locator).text

    @property
    def is_ask_a_question_present(self):
        return self.is_element_present(*self._support_question_link)
