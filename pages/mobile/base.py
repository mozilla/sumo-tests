#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page


class Base(Page):

    @property
    def header(self):
        return Base.HeaderRegion(self.testsetup)

    class HeaderRegion(Page):

        _dropdown_expanded_menu_locator = (By.CSS_SELECTOR, 'div.moz-menu')
        _menu_items_locator = (By.CSS_SELECTOR, '.menu-items li')
        _menu_button_locator = (By.CSS_SELECTOR, '.tab > a')

        def click_header_menu(self):
            self.selenium.find_element(*self._menu_button_locator).click()

        @property
        def is_dropdown_menu_expanded(self):
            return "expand" in self.selenium.find_element(*self._dropdown_expanded_menu_locator).get_attribute('class')

        @property
        def dropdown_menu_items(self):
            #returns a list containing all the menu items
            return [self.MenuItem(self.testsetup, web_element) for web_element in self.selenium.find_elements(*self._menu_items_locator)]

        class MenuItem(Page):

            _name_items_locator = (By.CSS_SELECTOR, 'a')

            def __init__(self, testsetup, element):
                Page.__init__(self, testsetup)
                self._root_element = element

            @property
            def name(self):
                return self._root_element.find_element(*self._name_items_locator).text
