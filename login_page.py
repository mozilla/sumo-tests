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
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
#                 Rebecca
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
'''
Created on Jun 30, 2010

@author: mozilla
'''
import sumo_test_data
import sumo_page

class LoginPage(sumo_page.SumoPage):
    """
        Form for login.
    """
    _page_title                    = 'Log In'
    _page_url                      = '/en-US/users/login'
    _username_box_locator          = 'id_username'
    _password_box_locator          = 'id_password'
    _log_in_button_locator         = "css=input[type='submit']"

    # if user is logged-in then you see these elements
    _logged_in_as_div_locator      = "css=div#mod-login_box > div"
    _logged_in_text                = "Logged in as"

    _non_admin_user_index          = 0
    _admin_user_index              = 1

    def go_to_login_page(self):
        self.open(self._page_url)
        self.is_the_current_page

    def log_in(self, uname, pwd):
        if not (self._page_title in self.selenium.get_title()):
            self.go_to_login_page()

        self.type(self._username_box_locator, uname)
        self.type(self._password_box_locator, pwd)
        self.click_button(self._log_in_button_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def log_in_as_admin(self):
        user_info = sumo_test_data.SUMOtestData().getUserInfo(self._admin_user_index)
        user_name = user_info['username']
        password = user_info['password']
        self.log_in(user_name, password)

    def log_in_as_non_admin(self):
        user_info = sumo_test_data.SUMOtestData().getUserInfo(self._non_admin_user_index)
        user_name = user_info['username']
        password = user_info['password']
        self.log_in(user_name, password)
