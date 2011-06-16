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
import re

import pytest

import forums_page
import login_page


class TestForumDeletion:

    @pytest.mark.bft
    @pytest.mark.fft
    def test_forum_deletion(self, testsetup):
        '''Checks bug 569310 (accidental forum deletion)'''
        login_page_obj   = login_page.LoginPage(testsetup)
        forums_page_obj  = forums_page.ForumsPage(testsetup)

        thread_num = str(random.randint(100, 10000))

        login_page_obj.log_in_as_admin()

        # Post a new thread
        thread_title = 'test_thread_%s' % thread_num
        thread_text = 'some text'

        forums_page_obj.go_to_forums_cat_list_page()
        forums_page_obj.click(forums_page_obj.first_cat_forum_link, True)
        forums_page_obj.post_new_thread_first_cat(thread_title, thread_text)

        thread_loc = str(forums_page_obj.get_url_current_page())
        thread_loc_arr = thread_loc.split('/')
        url1 = thread_loc_arr[len(thread_loc_arr) - 2]
        url2 = thread_loc_arr[len(thread_loc_arr) - 1]
        thread_loc = '%s/en-US/forums/%s/%s' % (testsetup.base_url_ssl, url1, url2)

        num_of_posts = 5

        for counter in range(1, (num_of_posts + 1)):
            thread_reply = 'some reply %s' % str(int(thread_num) + counter)
            forums_page_obj.post_reply(thread_loc, thread_reply)

        location = forums_page_obj.get_url_current_page()
        p = re.compile('post-[0-9]*')
        postString = p.search(location)
        postNum = postString.group()[5:]
        # delete link of second to last post
        post_to_delete_link = "css=li#post-%s > div > div > a:nth-child(2)" % str(int(postNum) - 1)
        forums_page_obj.wait_for_element_present(post_to_delete_link)
        forums_page_obj.click(post_to_delete_link, True)
        #confirmation dialogue for deletion
        forums_page_obj.click("css=form > input[type='submit']", True)
        forums_page_obj.open(thread_loc)
        assert forums_page_obj.is_text_present(thread_title)
