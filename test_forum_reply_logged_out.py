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

import forums_page


class TestForumReply:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    @pytest.mark.prod
    def test_forum_reply_logged_out(self, testsetup):
        """Tests to ensure Reply link is not available when logged-out
        """
        forums_page_obj = forums_page.ForumsPage(testsetup)

        forums_page_obj.go_to_forums_cat_list_page()
        forums_page_obj.click(forums_page_obj.first_cat_forum_link, True)

        counter = 0
        unlocked_not_found = True
        while unlocked_not_found and counter < 11:
            # click on a thread starting with the first and
            # work your way down the list until you have checked 10
            # thread and none of them are unlocked
            counter += 1
            if forums_page_obj.is_element_present(forums_page_obj.locked_thread_format % (counter)):
                continue
            else:
                unlocked_not_found = False
                forums_page_obj.click((forums_page_obj.unlocked_thread_format % (counter)), True)
                assert not forums_page_obj.is_element_present(forums_page_obj.reply_link),\
                          "Reply not disabled"
