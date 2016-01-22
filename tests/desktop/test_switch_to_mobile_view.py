# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.desktop.page_provider import PageProvider
from pages.mobile.page_provider import PageProvider as MobilePageProvider


class TestMobileSite:

    @pytest.mark.nondestructive
    def test_switch_to_mobile_view(self, base_url, selenium):
        home = PageProvider(base_url, selenium).home_page()
        home.switch_to_mobile_view()

        mobile = MobilePageProvider(base_url, selenium).home_page()
        assert mobile.is_mobile_view_displayed
