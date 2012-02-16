#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import Base


class ForumsPage(Base):
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
        self.selenium.click(self._post_new_thread_link)
        self.selenium.wait_for_page_to_load(self.timeout)
        self.selenium.type(self._thread_title_box, thread_title)
        self.selenium.type(self._thread_content_box, thread_content)
        self.selenium.click(self._post_button)
        self.selenium.wait_for_page_to_load(self.timeout)
        if not (self.selenium.is_text_present(thread_title)):
            raise Exception("Posting new thread failed\r\n")

    def go_to_forums_cat_list_page(self):
        self.selenium.open(self.forums_cat_list_url)
        self.selenium.wait_for_page_to_load(self.timeout)
        self.is_the_current_page

    def post_reply(self, thread_url, reply_text):
        self.go_to_thread(thread_url)
        self.selenium.type(self._thread_content_box, reply_text)
        self.selenium.click(self._reply_button)
        self.selenium.wait_for_page_to_load(self.timeout)
        if not(self.selenium.is_text_present(reply_text)):
            raise Exception('Posting reply failed\r\n')

    def go_to_thread(self, url):
        self.selenium.open(url)
        self.selenium.wait_for_page_to_load(self.timeout)
