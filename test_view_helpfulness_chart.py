#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from support_home_page import SupportHomePage
from knowledge_base_article import KnowledgeBaseArticle
from knowledge_base_article import KnowledgeBaseShowHistory
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
        kb_article = KnowledgeBaseArticle(mozwebqa)
        kb_article_history = KnowledgeBaseShowHistory(mozwebqa)

        sumo_homepage.go_to_support_home_page()
        sumo_homepage.click_first_top_issues_link()    
        
        kb_article.navigation.click_show_history()
        
        # verify article history page loaded
        Assert.true(kb_article_history.is_the_current_page)
        
        kb_article_history.click_show_helpfulness_chart()
        Assert.true(kb_article_history.is_helpfulness_chart_visible)
