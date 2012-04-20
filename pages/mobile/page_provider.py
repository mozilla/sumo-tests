#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page


class PageProvider(Page):
    """Internal methods."""

    def _go_to_page(self, page_object, do_login=False, user='default'):
        self.selenium.get(self.base_url_ssl + page_object._page_url)
        page_object.is_the_current_page
        if (do_login):
            page_object.sign_in(user)
        return page_object

    def home_page(self, do_login=False, user='default'):
        from pages.mobile.home import Home
        return self._go_to_page(Home(self.testsetup), do_login, user)

    def search_page(self, do_login=False, user='default'):
        from pages.mobile.search import Search
        return self._go_to_page(Search(self.testsetup), do_login, user)
