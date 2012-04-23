#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert

from pages.mobile.page_provider import PageProvider


class TestHome:

    expected_menu_items = ['MOZILLA FIREFOX', 'FEATURES', 'DESKTOP', 'ADD-ONS', 'SUPPORT', 'VISIT MOZILLA']

    @pytest.mark.nondestructive
    def test_the_expandable_header_menu(self, mozwebqa):
        home = PageProvider(mozwebqa).home_page()
        home.header.click_header_menu()
        Assert.true(home.header.is_dropdown_menu_expanded)

        menu_names = [menu.name for menu in home.header.dropdown_menu_items]
        Assert.equal(menu_names, self.expected_menu_items)

        home.header.click_header_menu()
        Assert.false(home.header.is_dropdown_menu_expanded)

    @pytest.mark.nondestructive
    def test_the_header_text_and_page_title(self, mozwebqa):
        home = PageProvider(mozwebqa).home_page()
        home.is_the_current_page

        Assert.equal('Firefox Help\nfor Mobile', home.header_text)
        Assert.equal('Return to Firefox Support homepage', home.header_title)
