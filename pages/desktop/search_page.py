#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base


class SearchPage(Base):
    """
    'Search for Firefox Help' page
    """

    _page_title = 'Search'
    _page_url = 'en-US/search'
    _search_box = "css=input.search-query"
    _search_button = "css=input[type='submit']"
    _refine_search_link = "css=a[href *= 'a=2']"
    _next_page_link = "link=*Next*"
    _prev_page_link = "link=*Previous*"
    _result_div = "css=div.result"
    _ask_a_question_locator = 'css=p.aaq'
    _support_question_link = "css=p.aaq > a"
    _second_page_link = "link=2"
    _search_unavailable_msg = "unavailable"
    _ten_search_results = "css=div.search-results div[class*='result']:nth-child(10)"
    _eleven_search_results = "css=div.search-results div[class*='result']:nth-child(11)"

    def go_to_search_page(self):
        self.selenium.open(self._page_url)
        self.selenium.wait_for_page_to_load(self.timeout)
        self.is_the_current_page

    def do_search_on_search_box(self, search_query):
        if not (self._page_title in self.selenium.get_title()):
            self.go_to_search_page()
        self.selenium.type(self._search_box, search_query)
        self.selenium.click(self._search_button)
        self.selenium.wait_for_page_to_load(self.timeout)

    def get_search_box_value(self):
        return self.selenium.get_value(self._search_box)

    def is_search_available(self):
        return not self.selenium.is_text_present(self._search_unavailable_msg)

    def is_result_present(self):
        return self.selenium.is_element_present(self._result_div)

    def are_ten_results_present(self):
        return self.selenium.is_element_present(self._ten_search_results) and not self.selenium.is_element_present(self._eleven_search_results)

    def click_refine_search_link(self, refine_search_page_obj):
        self.selenium.click(self._refine_search_link)
        self.selenium.wait_for_page_to_load(self.timeout)
        refine_search_page_obj.is_the_current_page

    def click_next_page_link(self):
        self.selenium.click(self._next_page_link)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def ask_a_question_text(self):
        return self.selenium.get_text(self._ask_a_question_locator)

    @property
    def is_ask_a_question_present(self):
        return self.selenium.is_element_present(self._support_question_link)
