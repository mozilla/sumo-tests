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

import login_page
import refine_search_page


class TestNoQueryAdvForumSearch:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    @pytest.mark.prod
    def test_no_query_adv_forum_search(self, mozwebqa):
        login_pg           = login_page.LoginPage(mozwebqa)
        refine_search_pg   = refine_search_page.RefineSearchPage(mozwebqa)

        login_pg.log_in_as_non_admin()
        refine_search_pg.go_to_refine_search_page()
        refine_search_pg.click(refine_search_pg.support_questions_tab)
        refine_search_pg.type(refine_search_pg.asked_by_box, login_pg.get_user_name_non_admin())
        refine_search_pg.click_button(refine_search_pg.search_button_support, True, mozwebqa.timeout)
        assert "refine" in mozwebqa.selenium.get_attribute(\
                           "css=div#basic-search > form > input:nth-child(13)@class"),\
                           "refine class not found"

