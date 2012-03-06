#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.support_home_page import SupportHomePage
from pages.desktop.knowledge_base_article import KnowledgeBaseArticle
from pages.desktop.knowledge_base_article import KnowledgeBaseShowHistory
import pytest

class TestViewHelpfulnessChart:

    @pytest.mark.fft
    def test_view_helpfulness_chart(self, mozwebqa):
        """
           Creates a new knowledge base article.
           Verifies creation.
           Deletes the article
        """
        sumo_homepage = SupportHomePage(mozwebqa)
        kb_article_history = KnowledgeBaseShowHistory(mozwebqa)

        # navigate to article
        sumo_homepage.go_to_page()
        sumo_homepage.sign_in();
        contrib_page = sumo_homepage.click_knowledge_base_dashboard_link()
        Assert.true(contrib_page.is_the_current_page)
        contrib_page.click_all_time()
        kb_article = contrib_page.click_top_visited_article_link()

        # vote on article to artificially inflate data
        kb_article.vote()

        kb_article.navigation.click_show_history()

        # verify article history page loaded
        Assert.true(kb_article_history.is_the_current_page)

        kb_article_history.click_show_helpfulness_chart()
        Assert.true(kb_article_history.is_helpfulness_chart_visible)
