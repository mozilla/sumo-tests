#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page
from selenium.webdriver.common.by import By


class Base(Page):

    @property
    def header(self):
        return self.HeaderRegion(self.testsetup)

    def sign_in(self, user="default"):
        login = self.header.click_login()
        login.log_in(user)


    def sign_out(self):
        self.header.click_logout()

    class HeaderRegion(Page):

        #Not LoggedIn
        _login_locator = (By.CSS_SELECTOR, 'li.logout > a:nth-of-type(1)')
        _register_locator = (By.CSS_SELECTOR, 'li.logout > a:nth-of-type(2)')

        #LoggedIn
        _account_controller_locator = (By.CSS_SELECTOR, '#aux-nav .account a.user')
        _account_dropdown_locator = (By.CSS_SELECTOR, '#aux-nav .account ul') # untested
        _logout_locator = (By.CSS_SELECTOR, '.logout > a')

        def click_login(self):
            self.selenium.find_element(*self._login_locator).click()
            from pages.desktop.login_page import LoginPage
            return LoginPage(self.testsetup)

        def click_logout(self):
            self.selenium.find_element(*self._logout_locator).click()

        @property
        def is_user_logged_in(self):
            return self.is_element_visible(*self._account_controller_locator)

