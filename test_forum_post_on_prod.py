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
import random

import pytest

import forums_page
import login_page


class TestForumPostProd:

    @pytest.mark.prod
    def test_forum_pagination_on_prod(self, testsetup):
        """Post a new thread and reply to the thread
        Check pagination after 20 posts.
        This test is suppossed to be run only on Production site.
        It Posts in the auto-test forums which is only viewable by certain users
        Note: This test will not run locally by itself. It will only run in BFT suite.
        """
        thread_num = str(random.randint(100, 10000))
        thread_title = 'test_thread_' + thread_num
        thread_text = 'some text'

        login_page_obj   = login_page.LoginPage(testsetup)
        forums_page_obj  = forums_page.ForumsPage(testsetup)

        login_page_obj.log_in_as_admin()

        # Post a new thread
        # this forum is only only viewable by certain users,
        # so posting to it on Prod is allowed.

        forums_page_obj.open('https://support.mozilla.com/en-US/forums/auto-test')
        forums_page_obj.post_new_thread_first_cat(thread_title, thread_text)

        assert (forums_page_obj.is_text_present(thread_text))

        forums_page_obj.log_out()
