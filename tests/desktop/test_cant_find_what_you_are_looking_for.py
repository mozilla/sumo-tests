#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
from pages.desktop.search_page import SearchPage
import pytest


class TestCantFindWhatYouAreLookingFor:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    @pytest.mark.prod
    def test_cant_find_what_youre_looking_for_test(self, mozwebqa):
        search_page_obj = SearchPage(mozwebqa)

        searchTerms = ["firefox", "bgkhdsaghb"]
        for current_search_term in searchTerms:
            search_page_obj.go_to_search_page()
            search_page_obj.do_search_on_search_box(current_search_term)

            expected_text = "Can't find what you're looking for?"
            Assert.contains(expected_text, search_page_obj.ask_a_question_text)
            Assert.true(search_page_obj.is_ask_a_question_present, "Ask question link not present")
