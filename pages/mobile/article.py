# !/ usr / bin / env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.mobile.base import Base


class Article(Base):

    _helpful_button_locator = (By.NAME, 'helpful')
    _helpful_form_text_locator = (By.CSS_SELECTOR, 'form.helpful > p > span')
    _vote_box_locator = (By.CSS_SELECTOR, 'div.ajax-vote-box')

    def __init__(self, testsetup):
        Base.__init__(self, testsetup)

    def click_helpful_button(self):
        self.selenium.find_element(*self._helpful_button_locator).click()

    @property
    def helpul_form_text(self):
        return self.selenium.find_element(*self._helpful_form_text_locator).text

    @property
    def is_vote_box_visible(self):
        return self.is_element_visible(*self._vote_box_locator)

    @property
    def vote_box_text(self):
        return self.selenium.find_element(*self._vote_box_locator).text
