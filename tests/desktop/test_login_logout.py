#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.page_provider import PageProvider

import pytest


class TestLoginLogout:

    @pytest.mark.nondestructive
    def test_login(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')

        Assert.true(home_page.header.is_user_logged_in, 'User not shown to be logged in')

    @pytest.mark.native
    @pytest.mark.nondestructive
    def test_logout(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page(do_login=True, user='default')
        Assert.true(home_page.header.is_user_logged_in, 'User not shown to be logged in')

        # sign out
        home_page.sign_out()
        Assert.false(home_page.header.is_user_logged_in)
