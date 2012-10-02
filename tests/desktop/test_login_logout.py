#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.desktop.page_provider import PageProvider
from mocks.mock_article import MockArticle


class TestLoginLogout:

    @pytest.mark.nondestructive
    def test_login(self, mozwebqa):
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')

        Assert.true(home_page.header.is_user_logged_in, 'User not shown to be logged in')

    ### logging out of the following pages redirects the user to the home page

    @pytest.mark.native
    @pytest.mark.nondestructive
    @pytest.mark.parametrize('page_method', ['home_page',
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
<<<<<<< HEAD
    @pytest.mark.destructive  # until the credentials are working on production
=======
>>>>>>> remove_destructive_for_issue_134
    def test_logout_from_new_kb_article_page(self, mozwebqa):
        new_kb_page = PageProvider(mozwebqa).new_kb_article_page()
        Assert.true(new_kb_page.header.is_user_logged_in, 'User not shown to be logged in')

        # sign out
        home_page = new_kb_page.sign_out()
        home_page.is_the_current_page
        Assert.false(home_page.header.is_user_logged_in)

    @pytest.mark.native
    def test_logout_from_edit_kb_article_page(self, mozwebqa):
        kb_new_article = PageProvider(mozwebqa).new_kb_article_page()

        # create a new article
        mock_article = MockArticle()
        kb_new_article.set_article(mock_article)
        kb_new_article.submit_article()
        kb_article_history = kb_new_article.set_article_comment_box(mock_article['comment'])

        kb_edit_article = kb_article_history.navigation.click_edit_article()

        # sign out
        home_page = kb_edit_article.sign_out()
        home_page.is_the_current_page
        Assert.false(home_page.header.is_user_logged_in)

    @pytest.mark.native
    def test_logout_from_translate_kb_article_page(self, mozwebqa):
        kb_new_article = PageProvider(mozwebqa).new_kb_article_page()

        # create a new article
        mock_article = MockArticle()
        kb_new_article.set_article(mock_article)
        kb_new_article.submit_article()
        kb_article_history = kb_new_article.set_article_comment_box(mock_article['comment'])

        kb_translate_pg = kb_article_history.navigation.click_translate_article()
        kb_translate_pg.click_translate_language('Esperanto (eo)')

        # sign out
        home_page = kb_translate_pg.sign_out()
        home_page.is_the_current_page
        Assert.false(home_page.header.is_user_logged_in)
