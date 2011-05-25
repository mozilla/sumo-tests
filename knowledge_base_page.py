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
# Mozilla
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

import sumo_page
import vars

page_load_timeout = vars.ConnectionParameters.page_load_timeout


class KBPage(sumo_page.SumoPage):
    """
    'Create New Article' Page is where the form
    for creating new knowledge base article is found.
    """
    _page_title                           = 'Create a New Article'
    _page_title_rev_hist                  = 'Revision History'
    _page_url_new_article                 = '/en-US/kb/new'

    _article_url                          = ''
    _article_history_url                  = ''
    _article_title                        = ''
    _article_title_box_locator            = 'id_title'
    _article_category_menu_locator        = 'id_category'
    _article_keywords_box_locator         = 'id_keywords'
    _article_summary_box_locator          = 'id_summary'
    _article_content_box_locator          = 'id_content'
    _article_preview_btn_locator          = 'btn-preview'
    _article_preview_content_locator      = "css=div#preview > div#doc-content"
    _article_submit_btn_locator           = 'btn-submit'
    _comment_box_locator                  = 'id_comment'
    _comment_submit_btn_locator           = "css=input[value='Submit']"

    _edit_article_link_locator            = "css=nav#doc-tabs > ul > li.edit:nth-child(3) > a[href*='edit']"
    _review_top_revision_link_locator     = "css=div#revision-list > form > ul > li:nth-child(1) > div.status > a"
    _edit_desc_link_locator               = "css=div#document-form > details > summary"

    _delete_document_link_locator         = "css=div#delete-doc > a[href*='delete']"
    _delete_confirmation_btn_locator      = "css=input[value='Delete']"

    def __init__(self, selenium):
        super(KBPage, self).__init__(selenium)  

    @property
    def article_summary_box(self):
        return self._article_summary_box_locator

    @property
    def article_content_box(self):
        return self._article_content_box_locator

    @property
    def page_title_revision_history(self):
        return self._page_title_rev_hist

    @property
    def article_url(self):
        return self._article_url

    @article_url.setter
    def article_url(self, url):
        self._article_url = url

    @property
    def article_title(self):
        return self._article_title

    @article_title.setter
    def article_title(self, title):
        self._article_title = title

    @property
    def article_history_url(self):
        return self._article_history_url

    @article_history_url.setter
    def article_history_url(self, hist_url):
        self._article_history_url = hist_url

    def go_to_article_history_page(self):
        self.open(self._article_history_url)

    def go_to_article_page(self):
        self.open(self._article_url)

    def go_to_create_new_article_page(self):
        self.open(vars.ConnectionParameters.baseurl_ssl + self._page_url_new_article)
        self.is_the_current_page

    def set_article(self, article_info_dict):
        """
            creates a new article
        """
        self.set_article_title(article_info_dict['title'])
        label_locator = "label=%s" % (article_info_dict['category'])
        self.set_article_category(label_locator)
        self.set_article_keyword(article_info_dict['keyword'])
        self.set_article_summary(article_info_dict['summary'])
        self.set_article_content(article_info_dict['content'])

    def edit_article(self, article_info_dict):
        """
            Edits an existing article.
        """
        self.set_article_keyword(article_info_dict['keyword'])
        self.set_article_summary(article_info_dict['summary'])
        self.set_article_content(article_info_dict['content'])
        self.submit_article()
        self.set_article_comment_box()

    def set_article_title(self, title):
        self.selenium.type(self._article_title_box_locator, title)
        self._article_title = title

    def set_article_category(self, category):
        self.selenium.select(self._article_category_menu_locator, category)

    def set_article_keyword(self, keyword):
        self.selenium.type(self._article_keywords_box_locator, keyword)

    def set_article_summary(self, summary):
        self.selenium.type(self._article_summary_box_locator, summary)

    def set_article_content(self, content):
        self.selenium.type(self._article_content_box_locator, content)

    def set_article_comment_box(self, comment='automated test'):
        self.selenium.type(self._comment_box_locator, comment)
        self.selenium.click(self._comment_submit_btn_locator)
        self.selenium.wait_for_page_to_load(page_load_timeout)

    def submit_article(self):
        self.selenium.click(self._article_submit_btn_locator)
        self.wait_for_element_present(self._comment_box_locator)

    def delete_entire_article_document(self):
        self.go_to_article_history_page()
        self.click_delete_entire_article_document()
        self.click_delete_confirmation_button()

    def get_article_summary_text(self):
        return self.selenium.get_text(self._article_summary_box_locator)

    def get_article_contents_box(self):
        return self.selenium.get_text(self._article_content_box_locator)

    def click_edit_article(self):
        self.click(self._edit_article_link_locator, True, page_load_timeout)

    def click_delete_entire_article_document(self):
        self.click(self._delete_document_link_locator, True, page_load_timeout)

    def click_delete_confirmation_button(self):
        self.click(self._delete_confirmation_btn_locator, True, page_load_timeout)

    def click_article_preview_button(self):
        self.selenium.click(self._article_preview_btn_locator)
        self.wait_for_element_present(self._article_preview_content_locator)

    def get_article_preview_text(self):
        return self.selenium.get_text(self._article_preview_content_locator)