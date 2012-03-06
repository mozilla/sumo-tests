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
    _documents_table_busy_locator = "css=table.documents.busy"
    _top_most_visited_article_locator = \
        "css=#most-visited-table > tr:nth-of-type(2) > td:nth-of-type(1) > a"


    def click_top_visited_article_link(self):
        self.selenium.click(self._top_most_visited_article_locator)
        self.selenium.wait_for_page_to_load(self.timeout)
        return KnowledgeBaseArticle(self.testsetup)

    def click_this_week(self):
        self.selenium.click(self._this_week_button_locator)
        self.wait_for_element_come_and_go(self._documents_table_busy_locator)

    def click_all_time(self):
        self.selenium.click(self._all_time_button_locator)
        self.wait_for_element_come_and_go(self._documents_table_busy_locator)
