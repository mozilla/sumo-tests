#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class SupportHomePage(Base):
    """
    The Firefox Support Home Page contains
    web elements and methods that can be
    performed on them.
    """

    _page_title = 'Mozilla Support | Firefox Help'
    _page_url = '/en-US/home'
    
    _main_search_box = (By.ID, 'q')
    _search_button = (By.CSS_SELECTOR, 'button.img-submit')
    _see_all_button = (By.ID, 'button-seeall')
    _top_helpful_content_locator = (By.CSS_SELECTOR, 'div#home-content-quick section ul > li > a')
    _top_issues_link_locator = (By.CSS_SELECTOR, '#home-content-explore ul > li > a')
    _kb_dashboard_link_locator = (By.LINK_TEXT, 'Knowledge Base Dashboard')

    def do_search_on_main_search_box(self, search_query):
        search_box = self.selenium.find_element(*self._main_search_box)
        search_box.clear()
        search_box.type_keys(search_query)
        self.selenium.find_element(*self._search_button).click()
        from search_page import SearchPage
        return SearchPage(self.testsetup)

    def click_top_common_content_link(self):
        self.selenium.find_element(*self._top_helpful_content_locator).click()

    def click_first_top_issues_link(self):
        self.selenium.find_element(*self._top_issues_link_locator).click()

    def click_knowledge_base_dashboard_link(self):
        self.selenium.find_element(*self._kb_dashboard_link_locator).click()
        from contributors_page import ContributorsPage
        return ContributorsPage(self.testsetup)
