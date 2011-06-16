#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla Support
#
# The Initial Developer of the Original Code is
# Mozilla Support
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Tanay
#                 Vishal
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import pytest

import search_page


class TestSearchNumResults:

    @pytest.mark.prod
    def test_search_num_results(self, testsetup):
        search_page_obj = search_page.SearchPage(testsetup)

        search_page_obj.go_to_search_page()

        search_terms = ["crashes", "firefox crashes"]
        for current_search_term in search_terms:
            search_page_obj.do_search_on_search_box(current_search_term)
            not_found = True
            counter = 0
            while(not_found and counter < 3):
                if not(search_page_obj.is_search_available()):
                    search_page_obj.refresh()
                    counter += 1
                else:
                    not_found = False

            # Verify that there are 10 results on the page
            # After that, click the "Next" link,
            # until we're at the end of the search results:

            counter = 1
            while (search_page_obj.is_element_present(search_page_obj.next_page_link) and counter < 11):
                assert search_page_obj.are_ten_results_present(), "Ten results not present for %s" % (current_search_term)
                search_page_obj.click(search_page_obj.next_page_link, True)

                # Verify that we have a Next link on this page, otherwise,
                # we're at the end of the results and don't need to
                # count the results anymore!
                counter += 1
