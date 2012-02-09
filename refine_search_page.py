#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
Created on Jun 30, 2010

@author: mozilla
'''
from sumo_page import SumoPage


class RefineSearchPage(SumoPage):
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
        self.open(self._page_url)
        self.is_the_current_page

    def click_support_questions_tab(self):
        self.click(self._support_questions_tab)

    def type_in_asked_by_box(self, text):
        self.type(self._asked_by_box, text)

    def click_search_button_support(self):
        self.click(self._search_button_support, True)

    def do_search_on_knowledge_base(self, search_query, search_page_obj):
        self.click(self._kb_tab)
        self.type(self.article_search_box, search_query)
        self.click(self._search_button_kb, True)
        search_page_obj.is_the_current_page

    def do_search_on_support_questions(self, search_query, search_page_obj):
        self.click(self._support_questions_tab)
        self.type(self.post_search_box, search_query)
        self.click(self._search_button_support, True)
        search_page_obj.is_the_current_page

    def do_search_tags_on_support_questions(self, search_query, search_page_obj):
        self.click(self._support_questions_tab)
        self.type(self._post_tags_box, search_query)
        self.click(self._search_button_support, True)
        search_page_obj.is_the_current_page

    def do_search_on_discussion_forums(self, search_query, search_page_obj):
        self.click(self._forums_tab)
        self.type(self._thread_search_box, search_query)
        self.click(self._search_button_disc, True)
        search_page_obj.is_the_current_page

    def is_kb_cat_checked(self):
        return self.selenium.is_checked(self._kb_cat_check_box)

    @property
    def search_result_count(self):
        return self.selenium.get_css_count(self._search_results_list)
