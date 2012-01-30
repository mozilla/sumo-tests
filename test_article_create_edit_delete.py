#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla Support
#
# The Initial Developer of the Original Code is
# Mozilla Support
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Tanay
#                 Vishal
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
from unittestzero import Assert
from knowledge_base_new_article import KnowledgeBaseNewArticle
from knowledge_base_article import KnowledgeBaseArticle
from knowledge_base_article import KnowledgeBaseShowHistory
from knowledge_base_article import KnowledgeBaseEditArticle
from knowledge_base_article import KnowledgeBaseTranslate
from login_page import LoginPage
import re
import pytest
import datetime
xfail = pytest.mark.xfail


class TestArticleCreateEditDelete:

    @pytest.mark.fft
    def test_that_article_can_be_created(self, mozwebqa):
        """
           Creates a new knowledge base article.
           Verifies creation.
           Deletes the article
        """
        kb_new_article = KnowledgeBaseNewArticle(mozwebqa)
        kb_article_history = KnowledgeBaseShowHistory(mozwebqa)
        kb_edit_article = KnowledgeBaseEditArticle(mozwebqa)
        login_pg = LoginPage(mozwebqa)

        # Admin account is used as he can delete the article
        login_pg.log_in('admin')

        article_info_dict = self._create_new_generic_article(kb_new_article)
        kb_new_article.submit_article()
        kb_new_article.set_article_comment_box()

        # verify article history
        Assert.true(kb_article_history.is_the_current_page)

        # verify article contents
        kb_article_history.navigation.click_edit_article()

        actual_summary_text = kb_edit_article.article_summary_text
        Assert.equal(article_info_dict['summary'], actual_summary_text)

        actual_contents_text = kb_edit_article.article_contents_text
        Assert.equal(article_info_dict['content'], actual_contents_text)

        # delete the same article
        kb_edit_article.navigation.click_show_history()
        kb_article_history.delete_entire_article_document()

    @xfail(reason='Bug 694614 - spurious failures')
    @pytest.mark.fft
    def test_that_article_can_be_edited(self, mozwebqa):
        """
           Creates a new knowledge base article.
           Verifies creation.
           Edits the article, verifies the edition.
           Deletes the article
        """
        kb_new_article = KnowledgeBaseNewArticle(mozwebqa)
        kb_article_history = KnowledgeBaseShowHistory(mozwebqa)
        kb_edit_article = KnowledgeBaseEditArticle(mozwebqa)
        login_pg = LoginPage(mozwebqa)

        # Admin account is used as he can delete the article
        login_pg.log_in('admin')

        article_info_dict = self._create_new_generic_article(kb_new_article)
        kb_new_article.submit_article()
        kb_new_article.set_article_comment_box()

        # verify article history
        Assert.true(kb_article_history.is_the_current_page)

        # edit that same article
        timestamp = datetime.datetime.now()
        edited_article_summary = "this is an automated summary__%s_edited" % timestamp
        edited_article_content = "automated content__%s_edited" % timestamp
        article_info_dict_edited = {'title': article_info_dict['title'],\
                                    'category': 'How to', 'keyword': 'test',\
                                    'summary': edited_article_summary, 'content': edited_article_content}

        kb_article_history.navigation.click_edit_article()
        kb_edit_article.edit_article(article_info_dict_edited)

        kb_article_history.navigation.click_edit_article()

        # verify the contents of the edited article
        actual_page_title = kb_edit_article.get_page_title()
        Assert.contains(article_info_dict_edited['title'], actual_page_title)

        actual_summary_text = kb_edit_article.article_summary_text
        Assert.equal(edited_article_summary, actual_summary_text)

        actual_content_text = kb_edit_article.article_contents_text
        Assert.equal(edited_article_content, actual_content_text)

        # delete the same article
        kb_edit_article.navigation.click_show_history()
        kb_article_history.delete_entire_article_document()

    @pytest.mark.fft
    def test_that_article_can_be_deleted(self, mozwebqa):
        """
           Creates a new knowledge base article.
           Deletes the article.
           Verifies the deletion.
        """
        kb_new_article = KnowledgeBaseNewArticle(mozwebqa)
        kb_article = KnowledgeBaseArticle(mozwebqa)
        kb_article_history = KnowledgeBaseShowHistory(mozwebqa)
        login_pg = LoginPage(mozwebqa)

        # Admin account is used as he can delete the article
        login_pg.log_in('admin')

        article_info_dict = self._create_new_generic_article(kb_new_article)

        kb_new_article.submit_article()
        kb_new_article.set_article_comment_box()

        # go to article and get URL
        kb_article_history.navigation.click_article()
        article_url = kb_article.get_url_current_page()

        # delete the same article
        kb_article.navigation.click_show_history()
        kb_article_history.delete_entire_article_document()

        kb_article_history.open(article_url)
        actual_page_title = kb_article_history.get_page_title()
        Assert.contains("Page Not Found", actual_page_title)

    @pytest.mark.fft
    def test_that_article_can_be_previewed_before_submitting(self, mozwebqa):

        kb_new_article = KnowledgeBaseNewArticle(mozwebqa)
        login_pg = LoginPage(mozwebqa)

        # Admin account is used as he can delete the article
        login_pg.log_in('admin')

        article_info_dict = self._create_new_generic_article(kb_new_article)

        kb_new_article.click_article_preview_button()
        actual_preview_text = kb_new_article.get_article_preview_text()

        Assert.equal(article_info_dict['content'], actual_preview_text)

        # Does not need to be deleted as it does not commit the article

    @pytest.mark.fft
    def test_that_article_can_be_translated(self, mozwebqa):
        """
           Creates a new knowledge base article.
           Translate article
        """
        kb_new_article = KnowledgeBaseNewArticle(mozwebqa)
        kb_article_history = KnowledgeBaseShowHistory(mozwebqa)
        kb_edit_article = KnowledgeBaseEditArticle(mozwebqa)
        kb_translate_pg = KnowledgeBaseTranslate(mozwebqa)
        login_pg = LoginPage(mozwebqa)
        timestamp = datetime.datetime.now()

        # Admin account is used as he can delete the article
        login_pg.log_in('admin')

        article_info_dict = self._create_new_generic_article(kb_new_article)
        kb_new_article.submit_article()
        kb_new_article.set_article_comment_box()

        # verify article history
        Assert.true(kb_article_history.is_the_current_page)

        kb_article_history.navigation.click_translate_article()
        kb_translate_pg.click_translate_language('Esperanto (eo)')

        kb_translate_pg.type_title('artikolo_titolo%s' % timestamp)
        kb_translate_pg.type_slug('artikolo_limako_%s' % timestamp)
        kb_translate_pg.click_submit_review()

        change_comment = 'artikolo sangoj %s' % timestamp
        kb_translate_pg.type_modal_describe_changes(change_comment)
        kb_translate_pg.click_modal_submit_changes_button()

        Assert.equal(change_comment, kb_article_history.most_recent_revision_comment)
        Assert.equal('Esperanto', kb_article_history.revision_history)

        kb_article_history.delete_entire_article_document()

    def _create_new_generic_article(self, kb_new_article):
        timestamp = datetime.datetime.now()

        article_name = "test_article_%s" % timestamp
        article_summary = "this is an automated summary_%s" % timestamp
        article_content = "automated content_%s" % timestamp

        article_info_dict = {'title': article_name,
                             'category': 'How to', 'keyword': 'test',
                             'summary': article_summary, 'content': article_content}

        # create a new article
        kb_new_article.go_to_create_new_article_page()
        kb_new_article.set_article(article_info_dict)

        return article_info_dict
