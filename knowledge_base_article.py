#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from base import Base
from page import Page


class KnowledgeBase(Base):

    @property
    def navigation(self):
        return self.Navigation(self.testsetup)

    class Navigation(Page):

        _article_locator = "link=Article"
        _edit_article_locator = "link=Edit Article"
        _translate_article_locator = "link=Translate Article"
        _show_history_locator = "link=Show History"

        def click_article(self):
            self.selenium.click(self._article_locator)
            self.selenium.wait_for_page_to_load(self.timeout)

        def click_edit_article(self):
            self.selenium.click(self._edit_article_locator)
            self.selenium.wait_for_page_to_load(self.timeout)

        def click_translate_article(self):
            self.selenium.click(self._translate_article_locator)
            self.selenium.wait_for_page_to_load(self.timeout)

        def click_show_history(self):
            self.selenium.click(self._show_history_locator)
            self.selenium.wait_for_page_to_load(self.timeout)


class KnowledgeBaseArticle(KnowledgeBase):

    _title_locator = "css=h1.title"

    @property
    def article_title(self):
        self.selenium.get_text(self._title_locator)


class KnowledgeBaseEditArticle(KnowledgeBase):

    _article_keywords_box_locator = "id=id_keywords"
    _article_summary_box_locator = "id=id_summary"
    _article_content_box_locator = "id=id_content"
    _article_submit_btn_locator = "id=btn-submit"
    _comment_box_locator = "id=id_comment"
    _comment_submit_btn_locator = "css=input[value='Submit']"

    @property
    def article_summary_text(self):
        return self.selenium.get_text(self._article_summary_box_locator)

    @property
    def article_contents_text(self):
        return self.selenium.get_text(self._article_content_box_locator)

    def edit_article(self, article_info_dict):
        """
            Edits an existing article.
        """
        self.set_article_keyword(article_info_dict['keyword'])
        self.set_article_summary(article_info_dict['summary'])
        self.set_article_content(article_info_dict['content'])
        self.submit_article()
        self.set_article_comment_box()

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


class KnowledgeBaseTranslate(KnowledgeBase):

    _description_title_locator = "id=id_title"
    _description_slug_locator = "id=id_slug"
    _preview_content_button_locator = "id=btn-preview"
    _submit_button_locator = "css=.btn-important"

    # 2 elements inside the modal popup
    _describe_changes_locator = "id=id_comment"
    _submit_changes_button_locator = "css=#submit-modal > input"

    def click_translate_language(self, language):
        self.selenium.click("link=%s" % language)
        self.selenium.wait_for_page_to_load(self.timeout)

    def type_title(self, text):
        self.selenium.type(self._description_title_locator, text)

    def type_slug(self, text):
        self.selenium.type(self._description_slug_locator, text)

    def click_submit_review(self):
        self.selenium.click(self._submit_button_locator)

    def type_modal_describe_changes(self, text):
        self.selenium.type(self._describe_changes_locator, text)

    def click_modal_submit_changes_button(self):
        self.selenium.click(self._submit_changes_button_locator)


class KnowledgeBaseShowHistory(KnowledgeBase):

    _page_title = 'Revision History'

    _delete_document_link_locator = "css=div#delete-doc > a[href*='delete']"
    _delete_confirmation_btn_locator = "css=input[value='Delete']"

    _revision_history_language_locator = 'css=div.choice-list ul li > span'

    #history of the test
    _top_revision_comment = "css=#revision-list li:nth-child(2) > div.comment"
    
    _show_chart_link_locator = 'id=show-chart'
    _helpfulness_chart_locator = 'id=helpful-chart'
    _helpfulness_chart_graph_locator = 'css=svg > rect'

    def click_show_helpfulness_chart(self):
        self.selenium.click(self._show_chart_link_locator)
        self.wait_for_element_visible(self._helpfulness_chart_locator)
        
    @property
    def is_helpfulness_chart_visible(self):
        # Because of bug 723575 there are two element checks to assert that the graph has actually loaded
        return self.selenium.is_visible(self._helpfulness_chart_locator) and self.selenium.is_visible(self._helpfulness_chart_graph_locator)

    def delete_entire_article_document(self):
        self.click_delete_entire_article_document()
        self.click_delete_confirmation_button()

    def click_delete_entire_article_document(self):
        self.selenium.click(self._delete_document_link_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def click_delete_confirmation_button(self):
        self.selenium.click(self._delete_confirmation_btn_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def most_recent_revision_comment(self):
        self.wait_for_element_visible(self._top_revision_comment)
        return self.selenium.get_text(self._top_revision_comment)

    @property
    def revision_history(self):
        return self.selenium.get_text(self._revision_history_language_locator)
