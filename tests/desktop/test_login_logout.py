#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.page_provider import PageProvider

import pytest


class TestLoginLogout:

    @pytest.mark.nondestructive
    def test_login(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')

        Assert.true(home_page.header.is_user_logged_in, 'User not shown to be logged in')

    ### logging out of the following pages redirects the user to the home page

    @pytest.mark.native
    @pytest.mark.nondestructive
    @pytest.mark.parametrize('page_method', [
            'home_page',
            'new_question_page',
            'questions_page',
            'search_page',
            'refine_search_page',
        ])
    def test_logout_from_pages(self, mozwebqa, page_method):
        page_under_test = getattr(PageProvider(mozwebqa), page_method)(do_login=True, user='default')
        Assert.true(page_under_test.header.is_user_logged_in, 'User not shown to be logged in')

        # sign out
        home_page = page_under_test.sign_out()
        home_page.is_the_current_page
        Assert.false(home_page.header.is_user_logged_in)

    @pytest.mark.native
    @pytest.mark.destructive  #until the credentials are working on production
    def test_logout_from_new_kb_article_page(self, mozwebqa):
        new_kb_page = PageProvider(mozwebqa).new_kb_article_page()
        Assert.true(new_kb_page.header.is_user_logged_in, 'User not shown to be logged in')

        # sign out
        home_page = new_kb_page.sign_out()
        home_page.is_the_current_page
        Assert.false(home_page.header.is_user_logged_in)

    @pytest.mark.native
    @pytest.mark.destructive
    def test_logout_from_edit_kb_article_page(self, mozwebqa):
        kb_article_history = self._create_new_kb_article(mozwebqa)
        kb_edit_article = kb_article_history.navigation.click_edit_article()

        # sign out
        home_page = kb_edit_article.sign_out()
        home_page.is_the_current_page
        Assert.false(home_page.header.is_user_logged_in)

    @pytest.mark.native
    @pytest.mark.destructive
    def test_logout_from_translate_kb_article_page(self, mozwebqa):
        kb_article_history = self._create_new_kb_article(mozwebqa)
        kb_translate_pg = kb_article_history.navigation.click_translate_article()
        kb_translate_pg.click_translate_language('Esperanto (eo)')

        # sign out
        home_page = kb_translate_pg.sign_out()
        home_page.is_the_current_page
        Assert.false(home_page.header.is_user_logged_in)

    def _create_new_kb_article(self, mozwebqa):
        kb_new_article = PageProvider(mozwebqa).new_kb_article_page()
        article_info_dict = self._create_new_generic_article(kb_new_article)
        kb_new_article.submit_article()
        kb_article_history = kb_new_article.set_article_comment_box()
        return kb_article_history

    def _create_new_generic_article(self, kb_new_article):
        import datetime
        timestamp = datetime.datetime.now()

        article_name = "test_article_%s" % timestamp
        article_summary = "this is an automated summary_%s" % timestamp
        article_content = "automated content_%s" % timestamp

        article_info_dict = {'title': article_name,
                             'category': 'How to', 'keyword': 'test',
                             'summary': article_summary, 'content': article_content}

        # create a new article
        kb_new_article.set_article(article_info_dict)

        return article_info_dict
