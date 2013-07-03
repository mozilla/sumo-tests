#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class SupportHomePage(Base):
    """
    The Firefox Support Home Page contains
    web elements and methods that can be
    performed on them.
    """

    _page_title = 'Mozilla Support'
    _page_url = '/en-US/home'

    _main_search_box = (By.ID, 'q')
    _search_button = (By.CSS_SELECTOR, 'button.img-submit')
    _see_all_button = (By.ID, 'button-seeall')
    _top_helpful_content_locator = (By.CSS_SELECTOR, 'div#home-content-quick section ul > li > a')
    _top_issues_link_locator = (By.CSS_SELECTOR, '#home-content-explore ul > li > a')
    _kb_dashboard_link_locator = (By.LINK_TEXT, 'Knowledge Base Dashboard')
    _for_contributors_locator = (By.CSS_SELECTOR, '#for-contributors h1')

    _navigation_locator = (By.CSS_SELECTOR, 'nav#aux-nav > ul')

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

    @property
    def is_for_contributors_expanded(self):
        return 'expanded' in self.selenium.find_element(*self._for_contributors_locator).get_attribute('class')

    def click_navigation_item(self, item_text, subitem_index=None):
        nav = self.selenium.find_element(*self._navigation_locator)
        ac = ActionChains(self.selenium)
        for item in nav.find_elements(By.CSS_SELECTOR, 'li'):
            if item.text == item_text:
                if subitem_index is None:
                    ac.click(item)
                else:
                    ac.move_to_element(item)
                    subitems = item.find_elements(By.CSS_SELECTOR, 'ul > li > a')
                    ac.click(subitems[subitem_index])
                break
        else:
            raise Exception('Navigation item %s not found.' % item_text)

        ac.perform()

    def click_knowledge_base_dashboard_link(self):
        self.click_navigation_item('CONTRIBUTOR TOOLS', subitem_index=4)
        from contributors_page import ContributorsPage
        return ContributorsPage(self.testsetup)
