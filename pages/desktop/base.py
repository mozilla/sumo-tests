#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page


class Base(Page):

    @property
    def header(self):
        return Base.HeaderRegion(self.testsetup)

    def sign_in(self, user="default"):
        login = self.header.click_login()
        login.log_in(user)

    def sign_out(self):
        if self.header.is_user_logged_in:
            self.header.click_logout()

    class HeaderRegion(Page):

        #Not LoggedIn
        _login_locator = "link=Sign In"
        _register_locator = "link=Register"

        #LoggedIn
        _account_controller_locator = "css=#aux-nav .account a.user"
        _account_dropdown_locator = "css=#aux-nav .account ul" # untested
        _logout_locator = "css=li.nomenu.logout > a"

        def click_login(self):
            self.selenium.click(self._login_locator)
            from pages.desktop.login_page import LoginPage
            return LoginPage(self.testsetup)

        def click_logout(self):
            self.selenium.click(self._logout_locator)

        @property
        def is_user_logged_in(self):
            return self.selenium.is_visible(self._account_controller_locator)

