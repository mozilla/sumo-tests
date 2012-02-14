#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
Created on Jun 30, 2010

@author: mozilla
'''
from sumo_page import SumoPage


class LoginPage(SumoPage):
    """
        Form for login.
    """
    _page_title = 'Log In'
    _page_url = '/en-US/users/login'
    _username_box_locator = 'id_username'
    _password_box_locator = 'id_password'
    _log_in_button_locator = "css=input[type='submit']"

    # if user is logged-in then you see these elements
    _logged_in_as_div_locator = "css=div#mod-login_box > div"
    _logged_in_text = "Logged in as"

    def go_to_login_page(self):
        self.selenium.open(self._page_url)
        self.is_the_current_page

    def log_in(self, user="default"):
        if not (self._page_title in self.selenium.get_title()):
            self.go_to_login_page()

        credentials = self.testsetup.credentials[user]

        self.selenium.type(self._username_box_locator, credentials['name'])
        self.selenium.type(self._password_box_locator, credentials['password'])
        self.selenium.click(self._log_in_button_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def get_user_name(self, user="default"):
        credentials = self.testsetup.credentials[user]
        return credentials['name']
