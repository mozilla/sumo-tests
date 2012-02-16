#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from pages.base import Base
import string
import random


class RegisterPage(Base):
    """
        Form for user registration.
    """
    _page_title = 'Register'
    _page_title_after_registration = 'Thank you for registering'
    _page_url = '/en-US/users/register'
    _username_box_locator = 'id_for_username'
    _password_box_locator = 'id_for_password'
    _password_repeat_box_locator = 'id_for_password2'
    _email_add_box_locator = 'id_for_email'
    _register_button_locator = "css=input.btn[value='Register']"

    def go_to_registration_page(self):
        self.selenium.open(self._page_url)
        self.selenium.wait_for_page_to_load(self.timeout)
        self.is_the_current_page

    def register_new_user(self):
        user_name = self.get_random_word(5)
        password = '1234'
        email = user_name + "@mozilla.com"
        self.selenium.type(self._username_box_locator, user_name)
        self.selenium.type(self._password_box_locator, password)
        self.selenium.type(self._password_repeat_box_locator, password)
        self.selenium.type(self._email_add_box_locator, email)
        self.selenium.click(self._register_button_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def get_random_word(self, length):
        random_word = ''
        for _ in range(length):
            random_word += random.choice(string.letters)
        return random_word
