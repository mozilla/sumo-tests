#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.mobile.home import Home


class TestSearch:

    positive_search_term = "firefox"
    negative_search_term = "fail to update firefox"

    @pytest.mark.nondestructive
    @pytest.mark.parametrize(('search_term'), [positive_search_term, negative_search_term])
    def test_that_positive_search_returns_results(self, mozwebqa, search_term):
        home = Home(mozwebqa)

        search_page = home.search_for(search_term)
        Assert.greater(len(search_page.results), 0)
