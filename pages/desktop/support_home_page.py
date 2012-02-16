#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import Base
import re
import time


class SupportHomePage(Base):
    """
    The Firefox Support Home Pgae contains
    web elements and methods that can be
    performed on them.
    """
    _page_title = "Firefox Support Home Page"
    _main_search_box = "id=q"
    _search_button = "css=button.img-submit"
    _see_all_button = "id=button-seeall"
    _top_helpful_content_locator = "css=div#home-content-quick section ul > li > a"
    _top_issues_link_locator = 'css=#home-content-explore ul > li > a'

    def go_to_support_home_page(self):
        self.selenium.open('/')
        self.selenium.wait_for_page_to_load(self.timeout)
        self.is_the_current_page

    def do_search_on_main_search_box(self, search_query, search_page_obj):
        if re.search(self._page_title, self.selenium.get_title()) is None:
            self.go_to_support_home_page()
        self.selenium.type(SupportHomePage.main_search_box, search_query)
        self.selenium.click(self._search_button)
        self.selenium.wait_for_page_to_load(self.timeout)

        count = 0
        while not self.selenium.is_text_present('results for %s' % search_query):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                self.record_error()
                raise Exception(search_query + " search page hasnt loaded")
        search_page_obj.is_the_current_page

    def click_top_common_content_link(self):
        self.selenium.click(self._top_helpful_content_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def click_first_top_issues_link(self):
        self.selenium.click(self._top_issues_link_locator)
        self.selenium.wait_for_page_to_load(self.timeout)
