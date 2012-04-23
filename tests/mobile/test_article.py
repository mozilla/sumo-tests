#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from unittestzero import Assert

from pages.mobile.page_provider import PageProvider


class TestArticle:

    def test_that_checks_the_vote_of_an_article(self, mozwebqa):
        home = PageProvider(mozwebqa).home_page()

        article_page = home.click_to_see_first_article()
        Assert.contains("How to | Firefox Help", article_page.page_title)
        Assert.equal("Was this article helpful?", article_page.helpul_form_text)

        article_page.click_helpful_button()
        Assert.true(article_page.is_vote_box_visible)
        Assert.equal(u"Glad to hear it \u2014 thanks for the feedback!", article_page.vote_box_text)
