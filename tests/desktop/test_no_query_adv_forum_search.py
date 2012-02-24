#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
from pages.desktop.refine_search_page import RefineSearchPage
import pytest
xfail = pytest.mark.xfail

class TestNoQueryAdvForumSearch:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    @xfail(reason='Bug 710361 - Empty/default advanced searches fail/time out')
    def test_no_query_adv_forum_search(self, mozwebqa):
        refine_search_pg = RefineSearchPage(mozwebqa)

        # go to page and log in
        refine_search_pg.go_to_refine_search_page()
        refine_search_pg.sign_in('default')

        # do test
        refine_search_pg.click_support_questions_tab()
        refine_search_pg.type_in_asked_by_box(login_pg.get_user_name('default'))
        refine_search_pg.click_search_button_support()

        Assert.true(refine_search_pg.search_result_count > 0, "No search results not found")

        # sign out
        refine_search_pg.sign_out()