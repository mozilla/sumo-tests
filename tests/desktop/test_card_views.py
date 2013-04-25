#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.desktop.page_provider import PageProvider

@pytest.mark.skipif("config.getvalue('base_url')=='https://support-dev.allizom.org'")
class TestCardViews:

    @pytest.mark.nondestructive
    def test_click_learn_the_basics(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        page_title = home_page.click_card_grid(home_page.learn_the_basics_locator)
        Assert.contains('Learn the Basics: get started ', page_title)
        page_title = home_page.click_card_grid(home_page.firefox_product_locator)
        Assert.contains('', page_title)

    @pytest.mark.nondestructive
    def test_click_download_migration(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        page_title = home_page.click_card_grid(home_page.download_migration_locator)
        Assert.contains('Download, install and migration', page_title)
        page_title = home_page.click_card_grid(home_page.firefox_product_locator)
        Assert.contains('Download, install and migration | Firefox Help', page_title)

    @pytest.mark.nondestructive
    def test_click_privacy_security(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        page_title = home_page.click_card_grid(home_page.privacy_security_locator)
        Assert.contains('Privacy and security settings', page_title)
        page_title = home_page.click_card_grid(home_page.firefox_product_locator)
        Assert.contains('Privacy and security settings | Firefox Help', page_title)

    @pytest.mark.nondestructive
    def test_click_customize_addons(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        page_title = home_page.click_card_grid(home_page.customize_addons_locator)
        Assert.contains('Customize controls, options and add-ons', page_title)
        page_title = home_page.click_card_grid(home_page.firefox_product_locator)
        Assert.contains('Customize controls, options and add-ons | Firefox Help', page_title)

    @pytest.mark.nondestructive
    def test_click_fix_slowness(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        page_title = home_page.click_card_grid(home_page.fix_slowness_locator)
        Assert.contains('Fix slowness, crashing, error messages and other problems', page_title)
        page_title = home_page.click_card_grid(home_page.firefox_product_locator)
        Assert.contains('Fix slowness, crashing, error messages and other problems | Firefox Help', page_title)

    @pytest.mark.nondestructive
    @pytest.mark.xfail(reason='Xfailing till Selenium 2.23.0 Firefox visibility issue is fixed')
    def test_click_get_support(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        page_title = home_page.click_card_grid(home_page.get_support_locator)
        Assert.contains('Get community support', page_title)
        home_page.sign_out()
