#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
Created on Jun 30, 2010

@author: mozilla
'''
from pages.desktop.base import Base
from selenium.webdriver.common.by import By
from unittestzero import Assert
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class LoginPage(Base):
    """
        Form for login.
    """
    _page_title = 'Log In | Firefox Help'
    _page_url = '/en-US/users/login'
    _username_box_locator = (By.ID, 'id_username')
    _password_box_locator = (By.ID, 'id_password')
    _log_in_button_locator = (By.CSS_SELECTOR, 'input[type="submit"]')
    _login_error_locator = (By.CSS_SELECTOR, 'ul.errorlist > li')

    # if user is logged-in then you see these elements
    _logged_in_as_div_locator = (By.CSS_SELECTOR, 'div#mod-login_box > div')
    _logged_in_text = 'Logged in as'

    def go_to_login_page(self):
        self.open(self._page_url)
        self.is_the_current_page

    def log_in(self, user='default'):
        if not (self._page_title in self.selenium.title):
            self.go_to_login_page()

        credentials = self.testsetup.credentials[user]

        self.selenium.find_element(*self._username_box_locator).send_keys(credentials['name'])
        self.selenium.find_element(*self._password_box_locator).send_keys(credentials['password'])
        self.selenium.find_element(*self._log_in_button_locator).click()
        
        error = ""
        try:
            error = self.selenium.find_element(*self._login_error_locator).text
        except NoSuchElementException, ElementNotVisibleException:
            '''no error, do nothing'''
        finally:
            if error != "":
                error = "login failed for %s\n" % credentials['name'] + error
                Assert.fail(error)