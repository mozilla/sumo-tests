#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from pages.desktop.base import Base
import string
import random
from selenium.webdriver.common.by import By


class RegisterPage(Base):
    """
        Form for user registration.
    """
    _page_title = 'Register | Mozilla Support'
    _page_title_after_registration = 'Thank you for registering'
    _page_url = '/en-US/users/register'
    _username_box_locator = (By.ID, 'id_for_username')
    _password_box_locator = (By.ID, 'id_for_password')
    _password_repeat_box_locator = (By.ID, 'id_for_password2')
    _email_add_box_locator = (By.ID, 'id_for_email')
    _register_button_locator = (By.CSS_SELECTOR, 'input.btn[value="Register"]')

    def register_new_user(self):
        user_name = self.get_random_word(5)
        password = '1234abCD'
        email = user_name + "@mozilla.com"
        self.selenium.find_element(*self._username_box_locator).send_keys(user_name)
        self.selenium.find_element(*self._password_box_locator).send_keys(password)
        self.selenium.find_element(*self._password_repeat_box_locator).send_keys(password)
        self.selenium.find_element(*self._email_add_box_locator).send_keys(email)
        self.selenium.find_element(*self._register_button_locator).click()

    def get_random_word(self, length):
        random_word = ''
        for _ in range(length):
            random_word += random.choice(string.letters)
        return random_word
