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
# Contributor(s): Vishal
#
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

import support_home_page
import search_page


class TestTikiSearchResult:

    @pytest.mark.prod
    def test_tiki_search_result(self, testsetup):
        support_home_page_obj = support_home_page.SupportHomePage(testsetup)
        search_page_obj       = search_page.SearchPage(testsetup)

        search_term = 'firefox crashes'
        support_home_page_obj.go_to_support_home_page()
        support_home_page_obj.do_search_on_main_search_box(search_term, search_page_obj)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if not(search_page_obj.is_element_present(search_page_obj.second_page_link)):
                search_page_obj.refresh()
                counter += 1
            else:
                not_found = False

        assert search_page_obj.is_element_present((search_page_obj.second_page_link)),\
               "Page-2 link not found"
        assert search_page_obj.is_element_present((search_page_obj.next_page_link)),\
               "Next Page link not found"
        assert search_term == search_page_obj.get_search_box_value(),\
                              "search term: %s not found on search box" % search_term
        assert search_page_obj.is_element_present(search_page_obj.result_div),\
                                                           "Results not present"
        assert search_page_obj.is_element_present(search_page_obj.support_question_link),\
               "link=supportquestion not found on search results page"
        assert search_page_obj.is_element_present(search_page_obj.kb_link),\
               "Firefox Help Home link not found on search results page"
        assert search_page_obj.is_element_present(search_page_obj.question_link),\
               "Ask a Question link not found on search results page"
