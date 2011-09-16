#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla Support
#
# The Initial Developer of the Original Code is
# Mozilla Support
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
from sumo_page import SumoPage
import string
import random


class RegisterPage(SumoPage):
    """
        Form for user registration.
    """
    page_title = 'Register'
    page_title_after_registration = 'Thank you for registering'
    page_url = '/en-US/users/register'
    username_box_locator = 'id_for_username'
    password_box_locator = 'id_for_password'
    password_repeat_box_locator = 'id_for_password2'
    email_add_box_locator = 'id_for_email'
    register_button_locator = "css=input.btn[value='Register']"

    def go_to_registration_page(self):
        self.open(self.page_url)
        self.is_the_current_page

    def register_new_user(self):
        user_name = self.get_random_word(5)
        password = '1234'
        email = user_name + "@mozilla.com"
        self.type(self.username_box_locator, user_name)
        self.type(self.password_box_locator, password)
        self.type(self.password_repeat_box_locator, password)
        self.type(self.email_add_box_locator, email)
        self.click_button(self.register_button_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def get_random_word(self, length):
        random_word = ''
        for _ in range(length):
            random_word += random.choice(string.letters)
        return random_word