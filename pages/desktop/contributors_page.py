#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base
from pages.desktop.knowledge_base_article import KnowledgeBaseArticle


class ContributorsPage(Base):
    """
    The Firefox Contributors Page contains
    web elements and methods that can be
    performed on them.
    """
    _page_title = '[All Products] Knowledge Base Dashboard | Mozilla Support'
    _page_url = '/en-US/contributors'

    _this_week_button_locator = (By.LINK_TEXT, 'This Week')
    _all_time_button_locator = (By.LINK_TEXT, 'All Time')
    _top_most_visited_article_locator = \
        (By.CSS_SELECTOR, '#most-visited-table > tr:last-of-type > td:nth-of-type(1) > a')

    def go_to_contributors_page(self):
        self.open(self._page_url)
        self.is_the_current_page

    def click_top_visited_article_link(self):
        self.selenium.find_element(*self._top_most_visited_article_locator).click()
        return KnowledgeBaseArticle(self.testsetup)

    def click_this_week(self):
        self.selenium.find_element(*self._this_week_button_locator).click()
        self.wait_for_ajax()

    def click_all_time(self):
        self.selenium.find_element(*self._all_time_button_locator).click()
        self.wait_for_ajax()
