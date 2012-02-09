#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from sumo_page import SumoPage
import string
import random


class RegisterPage(SumoPage):
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
        self.open(self._page_url)
        self.is_the_current_page

    def register_new_user(self):
        user_name = self.get_random_word(5)
        password = '1234'
        email = user_name + "@mozilla.com"
        self.type(self._username_box_locator, user_name)
        self.type(self._password_box_locator, password)
        self.type(self._password_repeat_box_locator, password)
        self.type(self._email_add_box_locator, email)
        self.click_button(self._register_button_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def get_random_word(self, length):
        random_word = ''
        for _ in range(length):
            random_word += random.choice(string.letters)
        return random_word
