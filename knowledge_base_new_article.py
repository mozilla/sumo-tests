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
#                 Zac Campbell
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
from sumo_page import SumoPage


class KnowledgeBaseNewArticle(SumoPage):
    """
    'Create New Article' Page is where the form
    for creating new knowledge base article is found.
    """
    _page_title = 'Create a New Article'
    _page_url_new_article = '/en-US/kb/new'

    _article_title_box_locator = 'id_title'
    _article_category_menu_locator = 'id_category'
    _article_keywords_box_locator = 'id_keywords'
    _article_summary_box_locator = 'id_summary'
    _article_content_box_locator = 'id_content'
    _article_preview_btn_locator = 'btn-preview'
    _article_preview_content_locator = "css=div#preview > div#doc-content"
    _article_submit_btn_locator = 'btn-submit'
    _comment_box_locator = 'id_comment'
    _comment_submit_btn_locator = "css=input[value='Submit']"

    def go_to_create_new_article_page(self):
        self.open(self.base_url_ssl + self._page_url_new_article)
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

    def set_article_title(self, title):
        self.selenium.type(self._article_title_box_locator, title)

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
        self.selenium.wait_for_page_to_load(self.timeout)

    def submit_article(self):
        self.selenium.click(self._article_submit_btn_locator)
        self.wait_for_element_present(self._comment_box_locator)

    def click_article_preview_button(self):
        self.selenium.click(self._article_preview_btn_locator)
        self.wait_for_element_present(self._article_preview_content_locator)

    def get_article_preview_text(self):
        return self.selenium.get_text(self._article_preview_content_locator)
