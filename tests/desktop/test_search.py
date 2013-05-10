#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
import pytest
from pages.desktop.page_provider import PageProvider


class TestSearch:

    @pytest.mark.native
    @pytest.mark.nondestructive
    def test_no_query_adv_forum_search(self, mozwebqa):
        if mozwebqa.base_url == 'https://support.mozilla.org':
            pytest.xfail(reason='Bug 710361 - Empty/default advanced searches fail/time out on support-dev.allizom.org')
        refine_search_pg = PageProvider(mozwebqa).refine_search_page()

        # do test
        refine_search_pg.click_support_questions_tab()
        refine_search_pg.type_in_asked_by_box(refine_search_pg.get_user_name('default'))
        refine_search_pg.click_search_button_support()

        Assert.true(refine_search_pg.search_result_count > 0, "No search results not found")
