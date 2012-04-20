#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.mobile.page_provider import PageProvider


class TestSearch:

    @pytest.mark.nondestructive
    def test_that_positive_search_returns_results(self, mozwebqa):
        home = PageProvider(mozwebqa).home_page()

        search_page = home.search_for("firefox")
        Assert.greater(len(search_page.results), 0)

    @pytest.mark.nondestructive
    def test_that_negative_search_does_not_return_results(self, mozwebqa):
        home = PageProvider(mozwebqa).home_page()

        search_page = home.search_for("frfx")
        Assert.equal(len(search_page.results), 0)
