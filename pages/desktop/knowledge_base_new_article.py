#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class KnowledgeBaseNewArticle(Base):
    """
    'Create New Article' Page is where the form
    for creating new knowledge base article is found.
    """
    _page_title = 'Create a New Article | Knowledge Base | Firefox Help'
    _page_url_new_article = '/en-US/kb/new'

    _article_title_box_locator = (By.ID, 'id_title')
    _article_category_menu_locator = (By.ID, 'id_category')
    _article_keywords_box_locator = (By.ID, 'id_keywords')
    _article_summary_box_locator = (By.ID, 'id_summary')
    _article_content_box_locator = (By.ID, 'id_content')
    _article_slug_box_locator = (By.ID, 'id_slug')
    _article_preview_btn_locator = (By.CSS_SELECTOR, 'div.submit > .btn-preview')
    _article_preview_content_locator = (By.CSS_SELECTOR, 'div#preview > div#doc-content')
    _article_submit_btn_locator = (By.CSS_SELECTOR, 'input[value="Submit for Review"]')
    _comment_box_locator = (By.ID, 'id_comment')
    _comment_submit_btn_locator = (By.CSS_SELECTOR, 'input[value="Submit"]')

    def go_to_create_new_article_page(self):
        self.open(self._page_url_new_article)
        self.is_the_current_page

    def set_article(self, article_info_dict):
        """
            creates a new article
        """
        self.set_article_title(article_info_dict['title'])
        self.set_article_slug(article_info_dict['title'])
        self.set_article_category(article_info_dict['category'])
        self.set_article_keyword(article_info_dict['keyword'])
        self.set_article_summary(article_info_dict['summary'])
        self.set_article_content(article_info_dict['content'])

    def set_article_title(self, title):
        self.selenium.find_element(*self._article_title_box_locator).send_keys(title)

    def set_article_slug(self, text):
        self.selenium.find_element(*self._article_slug_box_locator).send_keys(text)
        
    def set_article_category(self, category):
        select_box = Select(self.selenium.find_element(*self._article_category_menu_locator))
        select_box.select_by_visible_text(category)

    def set_article_keyword(self, keyword):
        self.selenium.find_element(*self._article_keywords_box_locator).send_keys(keyword)

    def set_article_summary(self, summary):
        self.selenium.find_element(*self._article_summary_box_locator).send_keys(summary)

    def set_article_content(self, content):
        self.selenium.find_element(*self._article_content_box_locator).send_keys(content)

    def set_article_comment_box(self, comment='automated test'):
        self.selenium.find_element(*self._comment_box_locator).send_keys(comment)
        self.selenium.find_element(*self._comment_submit_btn_locator).click()

    def submit_article(self):
        self.selenium.find_element(*self._article_submit_btn_locator).click()
        self.wait_for_element_present(*self._comment_box_locator)

    def click_article_preview_button(self):
        self.selenium.find_element(*self._article_preview_btn_locator).click()
        self.wait_for_element_present(*self._article_preview_content_locator)

    def get_article_preview_text(self):
        return self.selenium.find_element(*self._article_preview_content_locator).text
