#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class Base(Page):

    learn_the_basics_locator = (By.CSS_SELECTOR, '#help-topics > ul.card-grid >li:nth-of-type(1) > a.cf')
    download_migration_locator = (By.CSS_SELECTOR, '#help-topics > ul.card-grid >li:nth-of-type(2) > a.cf')
    privacy_security_locator = (By.CSS_SELECTOR, '#help-topics > ul.card-grid >li:nth-of-type(3) > a.cf')
    customize_addons_locator = (By.CSS_SELECTOR, '#help-topics > ul.card-grid >li:nth-of-type(4) > a.cf')
    fix_slowness_locator = (By.CSS_SELECTOR, '#help-topics > ul.card-grid >li:nth-of-type(5) > a.cf')
    get_support_locator = (By.CSS_SELECTOR, '#help-topics > ul.card-grid >li:nth-of-type(6) > a.cf')
    firefox_product_locator = (By.CSS_SELECTOR, '#product-cards > li:nth-of-type(1) > a')
    firefox_android_product_locator = (By.CSS_SELECTOR, '#product-cards > li:nth-of-type(2) > a')
    firefoxos_product_locator = (By.CSS_SELECTOR, '#product-cards > li:nth-of-type(3) > a')

    def __init__(self, testsetup):
        super(Base, self).__init__(testsetup)
        self.header.dismiss_staging_site_warning_if_present()

    def click_card_grid(self, locator):
        ActionChains(self.selenium).move_to_element(
            self.selenium.find_element(*locator)).click().perform()
        self.selenium.implicitly_wait(10)
        return self.selenium.title

    @property
    def header(self):
        return self.HeaderRegion(self.testsetup)

    def sign_out(self):
        self.header.click_logout()

    def sign_in(self, user):

        if type(user) is str:
            user = self.testsetup.credentials[user]

        from browserid import BrowserID
        self.header.click_login()
        browser_id = BrowserID(self.selenium, timeout=self.timeout)
        browser_id.sign_in(user['email'], user['password'])

        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.header.is_user_logged_in)

    def format_page_title(self, *title_segments):
        '''
            Create a page title by adding separators between title segments
            and ending with the base segment
            Usage:
                format_page_title('Forum')            returns 'Forum | Mozilla Support'
                format_page_title('Create New', 'KB') returns 'Create New | KB | Mozilla Support'
                format_page_title('', 'Forum')        returns ' | Forum | Mozilla Support'
                format_page_title()                   returns 'Mozilla Support'
        '''
        separator = ' | '
        page_title = 'Mozilla Support'
        segment_list = list(title_segments)
        segment_list.reverse()
        for title in segment_list:
            page_title = title + separator + page_title
        return page_title

    class HeaderRegion(Page):

        # Not LoggedIn
        _login_locator = (By.CSS_SELECTOR, '.browserid-login')
        _register_locator = (By.CSS_SELECTOR, 'a.register')

        # LoggedIn
        _account_controller_locator = (By.CSS_SELECTOR, '.user')
        _account_dropdown_locator = (By.CSS_SELECTOR, 'li.dropdown a.user')
        _logout_locator = (By.CSS_SELECTOR, 'li.dropdown > ul > li > a.sign-out')

        # Staging site warning
        _staging_site_warning_close_button_locator = (By.CSS_SELECTOR, '#stage-banner > div.close-button')

        def click_login(self):
            self.selenium.find_element(*self._login_locator).click()

        def click_logout(self):
            self.dismiss_staging_site_warning_if_present()
            ActionChains(self.selenium).move_to_element(
                self.selenium.find_element(*self._account_dropdown_locator)
            ).move_to_element(
                self.selenium.find_element(*self._logout_locator)
            ).click().perform()

        def dismiss_staging_site_warning_if_present(self):
            if self.is_element_present(*self._staging_site_warning_close_button_locator):
                if self.is_element_visible(*self._staging_site_warning_close_button_locator):
                    self.selenium.find_element(*self._staging_site_warning_close_button_locator).click()

        @property
        def is_user_logged_in(self):
            return self.is_element_visible(*self._account_controller_locator)

        @property
        def is_user_logged_out(self):
            return self.is_element_visible(*self._login_locator)
