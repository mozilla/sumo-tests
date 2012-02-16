#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import Base


class RefineSearchPage(Base):
    """
       'Advanced Search' page.
    """
    _page_title = 'Search'
    _page_url = '/en-US/search?a=2'
    _article_search_box = "kb_q"
    _post_search_box = 'support_q'
    _post_tags_box = 'id_q_tags'
    _thread_search_box = 'discussion_q'
    _search_button_kb = "css=input[name='w'][value='1']+div.submit-search > input[type='submit']"
    _search_button_support = "css=input[name='w'][value='2']+div.submit-search > input[type='submit']"
    _search_button_disc = "css=input[name='w'][value='4']+div.submit-search > input[type='submit']"
    _kb_cat_check_box = "css=input#id_category_0"
    _kb_tab = "css=div#search-tabs > ul > li:nth-child(1) > a"
    _support_questions_tab = "css=div#search-tabs > ul > li:nth-child(2) > a"
    _forums_tab = "css=div#search-tabs > ul > li:nth-child(3) > a"
    _asked_by_box = "id_asked_by"
    _search_results_list = "css=div.result.question"

    def go_to_refine_search_page(self):
        self.selenium.open(self._page_url)
        self.selenium.wait_for_page_to_load(self.timeout)
        self.is_the_current_page

    def click_support_questions_tab(self):
        self.selenium.click(self._support_questions_tab)

    def type_in_asked_by_box(self, text):
        self.selenium.type(self._asked_by_box, text)

    def click_search_button_support(self):
        self.selenium.click(self._search_button_support)
        self.selenium.wait_for_page_to_load(self.timeout)

    def do_search_on_knowledge_base(self, search_query, search_page_obj):
        self.selenium.click(self._kb_tab)
        self.selenium.type(self.article_search_box, search_query)
        self.selenium.click(self._search_button_kb)
        self.selenium.wait_for_page_to_load(self.timeout)
        search_page_obj.is_the_current_page

    def do_search_on_support_questions(self, search_query, search_page_obj):
        self.selenium.click(self._support_questions_tab)
        self.selenium.type(self.post_search_box, search_query)
        self.selenium.click(self._search_button_support)
        self.selenium.wait_for_page_to_load(self.timeout)
        search_page_obj.is_the_current_page

    def do_search_tags_on_support_questions(self, search_query, search_page_obj):
        self.selenium.click(self._support_questions_tab)
        self.selenium.type(self._post_tags_box, search_query)
        self.selenium.click(self._search_button_support)
        self.selenium.wait_for_page_to_load(self.timeout)
        search_page_obj.is_the_current_page

    def do_search_on_discussion_forums(self, search_query, search_page_obj):
        self.selenium.click(self._forums_tab)
        self.selenium.type(self._thread_search_box, search_query)
        self.selenium.click(self._search_button_disc)
        self.selenium.wait_for_page_to_load(self.timeout)
        search_page_obj.is_the_current_page

    def is_kb_cat_checked(self):
        return self.selenium.is_checked(self._kb_cat_check_box)

    @property
    def search_result_count(self):
        return self.selenium.get_css_count(self._search_results_list)
