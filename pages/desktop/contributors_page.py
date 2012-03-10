#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from pages.desktop.knowledge_base_article import KnowledgeBaseArticle
import re
import time
from selenium.webdriver.common.by import By

class ContributorsPage(Base):
    """
    The Firefox Contributors Page contains
    web elements and methods that can be
    performed on them.
    """
    _page_title = 'Contributor Dashboard | Firefox Help'
    _page_url = '/en-US/contributors'
    _this_week_button_locator = (By.LINK_TEXT, 'This Week')
    _all_time_button_locator = (By.LINK_TEXT, 'All Time')
    _documents_table_busy_locator = (By.CSS_SELECTOR, 'table.documents.busy')
    _top_most_visited_article_locator = \
        (By.CSS_SELECTOR, '#most-visited-table > tr:nth-of-type(2) > td:nth-of-type(1) > a')


    def go_to_contributors_page(self):
        self.open(self._page_url)
        self.is_the_current_page

    def click_top_visited_article_link(self):
        self.selenium.find_element(*self._top_most_visited_article_locator).click()
        return KnowledgeBaseArticle(self.testsetup)

    def click_this_week(self):
        self.selenium.find_element(*self._this_week_button_locator).click()
        self.wait_for_element_come_and_go(*self._documents_table_busy_locator)

    def click_all_time(self):
        self.selenium.find_element(*self._all_time_button_locator).click()
        self.wait_for_element_come_and_go(self._documents_table_busy_locator)
