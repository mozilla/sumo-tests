#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page


class Base(Page):

    _sign_in_locator = 'link=Sign In'

    def sign_in(self):
        self.selenium.click(self._sign_in_locator)
        self.selenium.wait_for_page_to_load(self.timeout)
