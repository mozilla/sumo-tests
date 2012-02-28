#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from pages.desktop.knowledge_base_article import KnowledgeBaseArticle
import re
import time


class ContributorsPage(Base):
    """
    The Firefox Contributors Page contains
    web elements and methods that can be
    performed on them.
    """
    _page_title = "Contributor Dashboard"
    _page_url = "/en-US/contributors"
    _this_week_button_locator = "link=This Week"
    _all_time_button_locator = "link=All Time"
    _top_most_visited_article_locator = \
        "css=#most-visited-table tbody > tr:nth-of-type(2) > td:nth-of-type(1) > a"


    def go_to_contributors_page(self):
        self.selenium.open(self._page_url)
        self.selenium.wait_for_page_to_load(self.timeout)
        self.is_the_current_page

    def click_top_visited_article_link(self):
        self.selenium.click(self._top_most_visited_article_locator)
        self.selenium.wait_for_page_to_load(self.timeout)
        return KnowledgeBaseArticle(self.testsetup)

    def click_this_week(self):
        self.selenium.click(self._this_week_button_locator)

    def click_all_time(self):
        self.selnium.click(self._all_time_button_locator)
