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
import time
import re

import sumo_page
import vars



page_load_timeout = vars.ConnectionParameters.page_load_timeout

class KBPage(sumo_page.SumoPage):
    """
    'Create New Article' Page is where the form
    for creating new knowledge base article is found.
    """
    _page_title                   = 'Create a New Article'
    _page_title_rev_hist          = 'Revision History'
    _page_url_new_article         = '/en-US/kb/new'
    
    _article_title_box            = 'id_title'
    _article_category_menu        = 'id_category'
    _article_keywords_box         = 'id_keywords'
    _article_summary_box          = 'id_summary'
    _article_content_box          = 'id_content'
    _article_preview_btn          = 'btn-preview'
    _article_submit_btn           = 'btn-submit'
    _comment_box                  = 'id_comment'
    _comment_submit_btn           = "css=input[value='Submit']"
    
    _edit_article_link            = 'link=Edit Article'
    _edit_top_revision_link       = "link=Edit"
    _review_top_revision_link     = "css=div#revision-list > form > ul > li:nth-child(1) > div.status > a"
    _edit_desc_link               = "css=div#document-form > details > summary"
    
    _delete_document_link         = "link=Delete this document"
    _delete_confirmation_btn      = "css=input[value='Delete']"
    
    def __init__(self,selenium):
        super(KBPage,self).__init__(selenium)               
        
    
    def go_to_create_new_article_page(self):
        self.open(vars.ConnectionParameters.baseurl_ssl+self._page_url_new_article)
        self.is_the_current_page
        
    def create_new_article(self, article_info_dict):
        self.selenium.type(self._article_title_box, article_info_dict['title'])
        label_locator = "label=%s" %(article_info_dict['category'])
        self.selenium.select(self._article_category_menu, label_locator)
        self.selenium.type(self._article_keywords_box, article_info_dict['keyword'])
        self.selenium.type(self._article_summary_box, article_info_dict['summary'])
        self.selenium.type(self._article_content_box, article_info_dict['content'])
        self.selenium.click(self._article_submit_btn)
        self.wait_for_element_present(self._comment_box)
        self.selenium.type(self._comment_box, "automated test")
        self.click(self._comment_submit_btn, True, page_load_timeout)

    
    def verify_article_contents(self,article_info_dict):
        """ 
            verify the contents of the article
        """
        self.is_text_present(article_info_dict['title'])
        assert(article_info_dict['summary']==self.selenium.get_text(self._article_summary_box))
        assert(article_info_dict['content']==self.selenium.get_text(self._article_content_box))
        
    def verify_article_history(self,article_history_url,article_name):
        actual_page_title = self.selenium.get_title()
        if re.search(article_name, actual_page_title, re.IGNORECASE) is None:
            self.selenium.open(article_history_url)
        
        if not (self._page_title_rev_hist in actual_page_title):
            raise Exception("Expected string: %s not found in title: %s" %(self._page_title_rev_hist,actual_page_title))
     
    def click_edit_article(self):
        self.click(self._edit_article_link, True, page_load_timeout)
    
    def click_delete_article(self):
        self.click(self._delete_document_link, True, page_load_timeout)
    
    def click_delete_confirmation_button(self):
        self.click(self._delete_confirmation_btn, True, page_load_timeout)
