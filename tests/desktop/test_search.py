#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
import pytest
from pages.desktop.page_provider import PageProvider

class TestSearch:

    @pytest.mark.nondestructive
    @pytest.mark.parametrize(('search_term'), [
        ('firefox'),
        ('bgkhdsaghb')])
    def test_cant_find_what_youre_looking_for_test(self, mozwebqa, search_term):
        search_page_obj = PageProvider(mozwebqa).search_page()
        search_page_obj.do_search_on_search_box(search_term)

        expected_text = "Can't find what you're looking for?"
        Assert.contains(expected_text, search_page_obj.ask_a_question_text)
        Assert.true(search_page_obj.is_ask_a_question_present, "Ask question link not present")

    @pytest.mark.xfail(reason='Bug 710361 - Empty/default advanced searches fail/time out')
    @pytest.mark.native
    def test_no_query_adv_forum_search(self, mozwebqa):
        refine_search_pg = PageProvider(mozwebqa).refine_search_page()

        # do test
        refine_search_pg.click_support_questions_tab()
        refine_search_pg.type_in_asked_by_box(refine_search_pg.get_user_name('default'))
        refine_search_pg.click_search_button_support()

        Assert.true(refine_search_pg.search_result_count > 0, "No search results not found")

        # sign out
        refine_search_pg.sign_out()
