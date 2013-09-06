#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base


class LoginPage(Base):
    """
    Page for Login.
    """
    _page_title = 'Log In / Register | Mozilla Support'
    _page_url = '/en-US/users/auth'