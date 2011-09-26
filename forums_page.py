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
# Portions created by the Initial Developer are Copyright (C) 2010
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
import sumo_page


class ForumsPage(sumo_page.SumoPage):
    """
    The Firefox Forums Page contains
    web elements and methods that can be
    performed on them. The page lists different
    categories of forums: SUMO community/Off-topic etc.
    """
    _page_title = 'Forums'
    _first_cat_forum_link = "css=div.name > a"
    _post_new_thread_link = "new-thread"
    _thread_title_box = "css=input#id_title"
    _thread_content_box = "id_content"
    _post_button = "css=input[value='Post']"
    _cancel_link = "link=Cancel"
    _reply_button = "css=input[value='Reply']"
    _reply_link = "css=a[href='#thread-reply']"
    _pagination_link = "css=ol.pagination"
    _next_page_link = "css=li.next"
    _prev_page_link = "css=li.prev"
    _locked_thread_format = "css=ol.threads li:nth-child(%d) > div > img[title='Locked']"
    _unlocked_thread_format = "css=ol.threads > li:nth-child(%d) > div:nth-child(2) > a"

    def __init__(self, testsetup):
        self.forums_cat_list_url = testsetup.base_url_ssl + '/en-US/forums'
        self.kb_articles_forum_url = testsetup.base_url_ssl + '/en-US/forums/knowledge-base-articles'
        super(ForumsPage, self).__init__(testsetup)

    def post_new_thread_first_cat(self, thread_title, thread_content):
        self.click(self._post_new_thread_link, True, self.timeout)
        self.selenium.type(self._thread_title_box, thread_title)
        self.selenium.type(self._thread_content_box, thread_content)
        self.click(self._post_button, True, self.timeout)
        if not (self.selenium.is_text_present(thread_title)):
            raise Exception("Posting new thread failed\r\n")

    def go_to_forums_cat_list_page(self):
        self.open(self.forums_cat_list_url)
        self.is_the_current_page

    def post_reply(self, thread_url, reply_text):
        self.go_to_thread(thread_url)
        self.selenium.type(self._thread_content_box, reply_text)
        self.click(self._reply_button, True, self.timeout)
        if not(self.selenium.is_text_present(reply_text)):
            raise Exception('Posting reply failed\r\n')

    def go_to_thread(self, url):
        self.open(url)
