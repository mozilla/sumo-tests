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
import random
import re

import pytest

import knowledge_base_page
import login_page


class TestArticleCreateEditDelete:

    @pytest.mark.fft
    def test_that_article_can_be_created(self, mozwebqa):
        """
           Creates a new knowledge base article.
           Verifies creation.
           Deletes the article
        """
        knowledge_base_pg = knowledge_base_page.KBPage(mozwebqa)
        login_pg = login_page.LoginPage(mozwebqa)

        # Admin account is used as he can delete the article
        login_pg.log_in_as_admin()

        random_num = random.randint(1000, 9999)
        article_name = "test_article_%s" % random_num

        article_info_dict = {'title': article_name,
                             'category': 'How to', 'keyword': 'test',
                             'summary': "this is an automated summary_%s" % random_num,
                             'content': "automated content__%s" % random_num}

        # create a new article
        knowledge_base_pg.go_to_create_new_article_page()
        knowledge_base_pg.set_article(article_info_dict)
        knowledge_base_pg.submit_article()
        knowledge_base_pg.set_article_comment_box()

        # verify article history
        article_history_url = knowledge_base_pg.get_url_current_page()
        knowledge_base_pg.article_history_url = article_history_url
        actual_page_title = knowledge_base_pg.get_page_title()
        if not (knowledge_base_pg.page_title_revision_history in actual_page_title):
            raise Exception("Expected string: %s not found in title: %s"\
                             % (knowledge_base_pg.page_title_revision_history, actual_page_title))

        # verify article contents
        knowledge_base_pg.article_url = (knowledge_base_pg.article_history_url).replace("/history", "")
        knowledge_base_pg.go_to_article_page()
        knowledge_base_pg.click_edit_article()

        edit_page_title = knowledge_base_pg.get_page_title()
        assert knowledge_base_pg.article_title in edit_page_title,\
               "%s not found in Page title %s" % (knowledge_base_pg.article_title, edit_page_title)
        actual_summary_text = knowledge_base_pg.get_article_summary_text()
        actual_contents_text = knowledge_base_pg.get_article_contents_box()
        assert article_info_dict['summary'] == actual_summary_text,\
               "Expected: %s Actual: %s"\
                % (article_info_dict['summary'], actual_summary_text)
        assert article_info_dict['content'] == actual_contents_text,\
               "Expected: %s Actual: %s"\
                % (article_info_dict['content'], actual_contents_text)

        # delete the same article
        knowledge_base_pg.delete_entire_article_document()

    @pytest.mark.fft
    def test_that_article_can_be_edited(self, mozwebqa):
        """
           Creates a new knowledge base article.
           Verifies creation.
           Edits the article, verifies the edition.
           Deletes the article
        """
        knowledge_base_pg = knowledge_base_page.KBPage(mozwebqa)
        login_pg = login_page.LoginPage(mozwebqa)

        #login with an Admin account as he can delete the article
        login_pg.log_in_as_admin()

        random_num = random.randint(1000, 9999)
        article_name = "test_article_%s" % random_num

        article_info_dict = {'title': article_name,
                             'category': 'How to',
                             'keyword': 'test',
                             'summary': "this is an automated summary_%s" % random_num,
                             'content': "automated content__%s" % random_num}

        # create a new article
        knowledge_base_pg.go_to_create_new_article_page()
        knowledge_base_pg.set_article(article_info_dict)
        knowledge_base_pg.submit_article()
        knowledge_base_pg.set_article_comment_box()

        # set article history url
        article_history_url = knowledge_base_pg.get_url_current_page()
        knowledge_base_pg.article_history_url = article_history_url

        article_history_url = knowledge_base_pg.article_history_url
        knowledge_base_pg.article_url = article_history_url.replace("/history", "")

        # edit that same article
        article_info_dict_edited = {'title': article_name,\
                                    'category': 'How to', 'keyword': 'test',\
                                    'summary': "this is an automated summary__%s_edited" % random_num,
                                    'content': "automated content__%s_edited" % random_num}
        knowledge_base_pg.click_edit_article()
        knowledge_base_pg.edit_article(article_info_dict_edited)
        knowledge_base_pg.go_to_article_page()
        knowledge_base_pg.click_edit_article()

        # verify the contents of the edited article
        edit_page_title = knowledge_base_pg.get_page_title()
        assert knowledge_base_pg.article_title in edit_page_title,\
               "%s not found in Page title %s" % (knowledge_base_pg.article_title, edit_page_title)
        actual_summary_text = knowledge_base_pg.get_article_summary_text()
        actual_contents_text = knowledge_base_pg.get_article_contents_box()
        assert article_info_dict_edited['summary'] == \
                                                      actual_summary_text, "Expected: %s Actual: %s"\
                                                       % (article_info_dict_edited['summary'], actual_summary_text)
        assert article_info_dict_edited['content'] == actual_contents_text, "Expected: %s Actual: %s"\
                                                                            % (article_info_dict_edited['content'], actual_contents_text)

        # delete the same article
        knowledge_base_pg.delete_entire_article_document()

    @pytest.mark.fft
    def test_that_article_can_be_deleted(self, mozwebqa):
        """
           Creates a new knowledge base article.
           Deletes the article.
           Verifies the deletion.
        """
        knowledge_base_pg = knowledge_base_page.KBPage(mozwebqa)
        login_pg = login_page.LoginPage(mozwebqa)

        #login with an Admin account as he can delete the article
        login_pg.log_in_as_admin()

        random_num = random.randint(1000, 9999)
        article_name = "test_article_%s" % random_num

        article_info_dict = {'title': article_name,
                             'category': 'How to', 'keyword': 'test',
                             'summary': "this is an automated summary_%s" % random_num,
                             'content': "automated content__%s" % random_num}

        # create a new article
        knowledge_base_pg.go_to_create_new_article_page()
        knowledge_base_pg.set_article(article_info_dict)
        knowledge_base_pg.submit_article()
        knowledge_base_pg.set_article_comment_box()

        # set article history url
        knowledge_base_pg.article_history_url = knowledge_base_pg.get_url_current_page()
        knowledge_base_pg.article_url = (knowledge_base_pg.article_history_url).replace("/history", "")

        # delete the same article
        knowledge_base_pg.delete_entire_article_document()
        knowledge_base_pg.go_to_article_page()
        actual_page_title = knowledge_base_pg.get_page_title()
        if re.search('Page Not Found', actual_page_title, re.I) is None:
            raise AssertionError('Page title is %s, was expecting %s' % (actual_page_title, 'Page Not Found'))

    @pytest.mark.fft
    @pytest.mark.prod
    def test_that_article_can_be_previewed_before_submitting(self, mozwebqa):
        knowledge_base_pg = knowledge_base_page.KBPage(mozwebqa)
        login_pg = login_page.LoginPage(mozwebqa)

        login_pg.log_in_as_non_admin()

        random_num = random.randint(1000, 9999)
        article_name = "test_article_%s" % random_num

        article_info_dict = {'title': article_name,
                             'category': 'How to', 'keyword': 'test',
                             'summary': "this is an automated summary_%s" % random_num,
                             'content': "automated content__%s" % random_num}

        # create a new article
        knowledge_base_pg.go_to_create_new_article_page()
        knowledge_base_pg.set_article(article_info_dict)
        knowledge_base_pg.click_article_preview_button()
        actual_preview_text = knowledge_base_pg.get_article_preview_text()

        assert actual_preview_text == article_info_dict['content'],\
                                      "Expected: %s Actual: %s" % (article_info_dict['content'], actual_preview_text)
