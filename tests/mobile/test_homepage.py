#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert

from pages.mobile.home import Home


class TestHome:

    @pytest.mark.nondestructive
    def test_the_header_text_and_page_title(self, mozwebqa):
        home = Home(mozwebqa)
        home.is_the_current_page

        Assert.equal('Firefox Help\nfor Mobile', home.header_text)
        Assert.equal('Return to Firefox Support homepage', home.header_title)
