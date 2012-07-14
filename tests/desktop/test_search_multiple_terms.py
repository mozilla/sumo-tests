#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import pytest
from pages.desktop.page_provider import PageProvider

class TestSearchMultipleTerms:

    @pytest.mark.nondestructive
    def test_search_returns_either_of_two_terms(self, mozwebqa):
        """Search looks for either of two search terms

        Search for a good search term with a junk search term
        Should return same results as only the good search term

        """

        good_search_term = "firefox"
        junk_search_term = "werpadfjka"

        search_page_obj = PageProvider(mozwebqa).search_page()

        # search with good search term only.  save first search result.
        search_page_obj.do_search_on_search_box(good_search_term)
        # *** Recommend the SearchPage class have a method that returns search result ***
        result_first_search = search_page_obj.selenium.find_element(
            *search_page_obj._result_div).text

        # search with junk search term following the good search term
        search_page_obj.do_search_on_search_box(" " + junk_search_term)
        result_second_search = search_page_obj.selenium.find_element(
            *search_page_obj._result_div).text

        Assert.true(result_first_search == result_second_search,
                    "Similar searches have different results")