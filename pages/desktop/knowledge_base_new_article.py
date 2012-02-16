#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import Base


class KnowledgeBaseNewArticle(Base):
    """
    'Create New Article' Page is where the form
    for creating new knowledge base article is found.
    """
    _page_title = 'Create a New Article'
    _page_url_new_article = '/en-US/kb/new'

    _article_title_box_locator = 'id_title'
    _article_category_menu_locator = 'id_category'
    _article_keywords_box_locator = 'id_keywords'
    _article_summary_box_locator = 'id_summary'
    _article_content_box_locator = 'id_content'
    _article_preview_btn_locator = 'css=div.submit > .btn-preview'
    _article_preview_content_locator = "css=div#preview > div#doc-content"
    _article_submit_btn_locator = 'css=.btn-important'
    _comment_box_locator = 'id_comment'
    _comment_submit_btn_locator = "css=input[value='Submit']"

    def go_to_create_new_article_page(self):
        self.selenium.open(self.base_url_ssl + self._page_url_new_article)
        self.selenium.wait_for_page_to_load(self.timeout)
        self.is_the_current_page

    def set_article(self, article_info_dict):
        """
            creates a new article
        """
        self.set_article_title(article_info_dict['title'])
        label_locator = "label=%s" % (article_info_dict['category'])
        self.set_article_category(label_locator)
        self.set_article_keyword(article_info_dict['keyword'])
        self.set_article_summary(article_info_dict['summary'])
        self.set_article_content(article_info_dict['content'])

    def set_article_title(self, title):
        self.selenium.type(self._article_title_box_locator, title)

    def set_article_category(self, category):
        self.selenium.select(self._article_category_menu_locator, category)

    def set_article_keyword(self, keyword):
        self.selenium.type(self._article_keywords_box_locator, keyword)

    def set_article_summary(self, summary):
        self.selenium.type(self._article_summary_box_locator, summary)

    def set_article_content(self, content):
        self.selenium.type(self._article_content_box_locator, content)

    def set_article_comment_box(self, comment='automated test'):
        self.selenium.type(self._comment_box_locator, comment)
        self.selenium.click(self._comment_submit_btn_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def submit_article(self):
        self.selenium.click(self._article_submit_btn_locator)
        self.wait_for_element_present(self._comment_box_locator)

    def click_article_preview_button(self):
        self.selenium.click(self._article_preview_btn_locator)
        self.wait_for_element_present(self._article_preview_content_locator)

    def get_article_preview_text(self):
        return self.selenium.get_text(self._article_preview_content_locator)
