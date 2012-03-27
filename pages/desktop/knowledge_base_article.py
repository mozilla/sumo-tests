#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from pages.page import Page
from selenium.webdriver.common.by import By
from unittestzero import Assert


class KnowledgeBase(Base):

    @property
    def navigation(self):
        return self.Navigation(self.testsetup)

    @property
    def is_the_current_page(self):
        if self._page_title:
            page_title = self.page_title
            Assert.contains(self._page_title, page_title)

    class Navigation(Page):

        _article_locator = (By.LINK_TEXT, 'Article')
        _edit_article_locator = (By.LINK_TEXT, 'Edit Article')
        _translate_article_locator = (By.LINK_TEXT, 'Translate Article')
        _show_history_locator = (By.LINK_TEXT, 'Show History')
        _show_editing_tools_locator = (By.CSS_SELECTOR, '.show')
        _editing_tools_locator = (By.ID, 'doc-tabs')

        def show_editing_tools(self):
            if self.is_element_visible(*self._show_editing_tools_locator):
                self.selenium.find_element(*self._show_editing_tools_locator).click()
                self.wait_for_element_visible(*self._editing_tools_locator)
            
        def click_article(self):
            self.show_editing_tools()
            self.selenium.find_element(*self._article_locator).click()
            kb_article = KnowledgeBaseArticle(self.testsetup)
            kb_article.is_the_current_page
            return kb_article

        def click_edit_article(self):
            self.show_editing_tools()
            self.selenium.find_element(*self._edit_article_locator).click()
            edit_kb_article = KnowledgeBaseEditArticle(self.testsetup)
            edit_kb_article.is_the_current_page
            return edit_kb_article

        def click_translate_article(self):
            self.show_editing_tools()
            self.selenium.find_element(*self._translate_article_locator).click()
            translate_kb_article = KnowledgeBaseTranslate(self.testsetup)
            translate_kb_article.is_the_current_page
            return translate_kb_article

        def click_show_history(self):
            self.show_editing_tools()
            self.selenium.find_element(*self._show_history_locator).click()
            kb_article_history = KnowledgeBaseShowHistory(self.testsetup)
            kb_article_history.is_the_current_page
            return kb_article_history


class KnowledgeBaseArticle(KnowledgeBase):

    _page_title = ' | How to | Firefox Help'
    _title_locator = (By.CSS_SELECTOR, 'h1.title')
    _helpful_locator = (By.CSS_SELECTOR, 'div#side input[name=helpful]')
    _not_helpful_locator = (By.CSS_SELECTOR, 'div#side input[name=not-helpful]')
    _helpful_form_busy_locator = (By.CSS_SELECTOR, 'form.helpful.busy')

    @property
    def article_title(self):
        self.selenium.find_element(*self._title_locator).click()

    def vote_helpful(self):
        self.selenium.find_element(*self._helpful_locator).click()
        self.wait_for_ajax()

    def vote_not_helpful(self):
        self.selenium.find_element(*self._not_helpful_locator).click()
        self.wait_for_ajax()

    # each user can only vote once per article
    @property
    def can_vote(self):
        return self.is_element_present(*self._helpful_locator)

    # for providing some random feedback about the article
    def vote(self):
        if self.can_vote:
            import random
            helpful = random.randint(0,1)
            if (helpful):
                self.vote_helpful()
            else:
                self.vote_not_helpful()


class KnowledgeBaseEditArticle(KnowledgeBase):

    _page_title = 'Edit Article | '
    _article_keywords_box_locator = (By.ID, 'id_keywords')
    _article_summary_box_locator = (By.ID, 'id_summary')
    _article_content_box_locator = (By.ID, 'id_content')
    _article_submit_btn_locator = (By.CSS_SELECTOR, '.btn-submit')
    _comment_box_locator = (By.ID, 'id_comment')
    _comment_submit_btn_locator = (By.CSS_SELECTOR, 'input[value="Submit"]')

    @property
    def article_summary_text(self):
        return self.selenium.find_element(*self._article_summary_box_locator).text

    @property
    def article_contents_text(self):
        return self.selenium.find_element(*self._article_content_box_locator).text

    def edit_article(self, article_info_dict):
        """
            Edits an existing article.
        """
        self.set_article_keyword(article_info_dict['keyword'])
        self.set_article_summary(article_info_dict['summary'])
        self.set_article_content(article_info_dict['content'])
        self.submit_article()
        return self.set_article_comment_box()

    def set_article_keyword(self, keyword):
        element = self.selenium.find_element(*self._article_keywords_box_locator)
        element.clear()
        element.send_keys(keyword)

    def set_article_summary(self, summary):
        element = self.selenium.find_element(*self._article_summary_box_locator)
        element.clear()
        element.send_keys(summary)

    def set_article_content(self, content):
        element = self.selenium.find_element(*self._article_content_box_locator)
        element.clear()
        element.send_keys(content)

    def set_article_comment_box(self, comment='automated test'):
        self.selenium.find_element(*self._comment_box_locator).send_keys(comment)
        self.selenium.find_element(*self._comment_submit_btn_locator).click()
        kb_article_history = KnowledgeBaseShowHistory(self.testsetup)
        kb_article_history.is_the_current_page
        return kb_article_history

    def submit_article(self):
        self.selenium.find_element(*self._article_submit_btn_locator).click()
        self.wait_for_element_present(*self._comment_box_locator)


class KnowledgeBaseTranslate(KnowledgeBase):

    _page_title = 'Select language | '
    _description_title_locator = (By.ID, 'id_title')
    _description_slug_locator = (By.ID, 'id_slug')
    _preview_content_button_locator = (By.ID, 'btn-preview')
    _submit_button_locator = (By.CSS_SELECTOR, '.btn-important')

    # 2 elements inside the modal popup
    _describe_changes_locator = (By.ID, 'id_comment')
    _submit_changes_button_locator = (By.CSS_SELECTOR, '#submit-modal > input')

    def click_translate_language(self, language):
        self.selenium.find_element(By.LINK_TEXT, language).click()

    def type_title(self, text):
        self.selenium.find_element(*self._description_title_locator).send_keys(text)

    def type_slug(self, text):
        self.selenium.find_element(*self._description_slug_locator).send_keys(text)

    def click_submit_review(self):
        self.selenium.find_element(*self._submit_button_locator).click()

    def type_modal_describe_changes(self, text):
        self.selenium.find_element(*self._describe_changes_locator).send_keys(text)

    def click_modal_submit_changes_button(self):
        self.selenium.find_element(*self._submit_changes_button_locator).click()
        kb_article_history = KnowledgeBaseShowHistory(self.testsetup)
        kb_article_history.is_the_current_page
        return kb_article_history


class KnowledgeBaseShowHistory(KnowledgeBase):

    _page_title = 'Revision History | '

    _delete_document_link_locator = (By.CSS_SELECTOR, 'div#delete-doc > a[href*="delete"]')
    _delete_confirmation_btn_locator = (By.CSS_SELECTOR, 'input[value="Delete"]')

    _revision_history_language_locator = (By.CSS_SELECTOR, 'div.choice-list ul li > span')

    #history of the test
    _top_revision_comment = (By.CSS_SELECTOR, \
                             '#revision-list li:nth-child(2) > div.comment')

    _show_chart_link_locator = (By.ID, 'show-chart')
    _helpfulness_chart_locator = (By.ID, 'helpful-chart')
    _helpfulness_chart_graph_locator = (By.CSS_SELECTOR, 'svg > rect')

    @property
    def is_helpfulness_chart_visible(self):
        # Because of bug 723575 there are two element checks to assert that 
        # the graph has actually loaded
        return self.is_element_visible(*self._helpfulness_chart_locator) \
            and self.is_element_visible(*self._helpfulness_chart_graph_locator)

    def delete_entire_article_document(self):
        self.click_delete_entire_article_document()
        self.click_delete_confirmation_button()

    def click_delete_entire_article_document(self):
        self.selenium.find_element(*self._delete_document_link_locator).click()

    def click_delete_confirmation_button(self):
        self.selenium.find_element(*self._delete_confirmation_btn_locator).click()

    def click_show_helpfulness_chart(self):
        self.selenium.find_element(*self._show_chart_link_locator).click()
        self.wait_for_ajax()
        
    @property
    def most_recent_revision_comment(self):
        self.wait_for_element_visible(*self._top_revision_comment)
        return self.selenium.find_element(*self._top_revision_comment).text

    @property
    def revision_history(self):
        return self.selenium.find_element(*self._revision_history_language_locator).text
