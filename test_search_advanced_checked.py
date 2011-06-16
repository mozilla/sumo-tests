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

import search_page
import refine_search_page


class TestAdvancedSearchChecked:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    @pytest.mark.prod
    def test_advanced_search_checked(self, testsetup):
        refine_search_page_obj     = refine_search_page.RefineSearchPage(testsetup)
        search_page_obj            = search_page.SearchPage(testsetup)

        refine_search_page_obj.go_to_refine_search_page()
        assert refine_search_page_obj.is_kb_cat_checked(),\
               "Default search forum is not set to Firefox"

        search_word = 'firefox crashes'
        # search kb tab
        refine_search_page_obj.do_search_on_knowledge_base(search_word, search_page_obj)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter += 1
            else:
                not_found = False
        search_page_obj.is_the_current_page

        # search support questions tab
        refine_search_page_obj.go_to_refine_search_page()
        refine_search_page_obj.do_search_on_support_questions(search_word, search_page_obj)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter += 1
            else:
                not_found = False
        search_page_obj.is_the_current_page

        # search discussion forums tab
        refine_search_page_obj.go_to_refine_search_page()
        refine_search_page_obj.do_search_on_discussion_forums(search_word, search_page_obj)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter += 1
            else:
                not_found = False
        search_page_obj.is_the_current_page
