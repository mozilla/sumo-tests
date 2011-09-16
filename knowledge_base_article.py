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
# Contributor(s): Zac Campbell
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


class KnowledgeBase(SumoPage):
    
    @property
    def navigation(self):
        return self.Navigation(self.testsetup)
    
    class Navigation(SumoPage):
        
        article_locator = "link=Article"
        edit_article_locator = "link=Edit Article"
        translate_article_locator = "link=Translate Article"
        show_history_locator = "link=Show History"
        
        def click_article(self):
            self.click(self.article_locator, True, self.timeout)
        
        def click_edit_article(self):
            self.click(self.edit_article_locator, True, self.timeout)
        
        def click_translate_article(self):
            self.click(self.translate_article_locator, True, self.timeout)
        
        def click_show_history(self):
            self.click(self.show_history_locator, True, self.timeout)


class KnowledgeBaseArticle(KnowledgeBase):

    title_locator = "css=h1.title"
    
    @property
    def article_title(self):
        self.get_text(self.title_locator)


class KnowledgeBaseEditArticle(KnowledgeBase):
    
    article_keywords_box_locator = 'id_keywords'
    article_summary_box_locator = 'id_summary'
    article_content_box_locator = 'id_content'
    article_submit_btn_locator = 'btn-submit'
    comment_box_locator = 'id_comment'
    comment_submit_btn_locator = "css=input[value='Submit']"        
        
    @property
    def article_summary_text(self):
        return self.get_text(self.article_summary_box_locator)

    @property
    def article_contents_text(self):
        return self.get_text(self.article_content_box_locator)
        
    def edit_article(self, article_info_dict):
        """
            Edits an existing article.
        """
        self.set_article_keyword(article_info_dict['keyword'])
        self.set_article_summary(article_info_dict['summary'])
        self.set_article_content(article_info_dict['content'])
        self.submit_article()
        self.set_article_comment_box()
        
    def set_article_keyword(self, keyword):
        self.selenium.type(self.article_keywords_box_locator, keyword)

    def set_article_summary(self, summary):
        self.selenium.type(self.article_summary_box_locator, summary)

    def set_article_content(self, content):
        self.selenium.type(self.article_content_box_locator, content)

    def set_article_comment_box(self, comment='automated test'):
        self.selenium.type(self.comment_box_locator, comment)
        self.selenium.click(self.comment_submit_btn_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def submit_article(self):
        self.selenium.click(self.article_submit_btn_locator)
        self.wait_for_element_present(self.comment_box_locator)
        

class KnowledgeBaseTranslate(KnowledgeBase):
        
    description_title_locator = "id_title"
    description_slug_locator = "id_slug"
    preview_content_button_locator = "btn-preview"
    submit_button_locator = "btn-submit"
    
    # 2 elements inside the modal popup
    describe_changes_locator = "id_comment"
    submit_changes_button_locator = "css=#submit-modal > input"
    
    def click_translate_language(self, language):
        self.click("link=%s" % language, True, self.timeout)
    
    def type_title(self, text):
        self.type(self.description_title_locator, text)
    
    def type_slug(self, text):
        self.type(self.description_slug_locator, text)
        
    def click_submit_review(self):
        self.click(self.submit_button_locator)
        
    def type_modal_describe_changes(self, text):
        self.type(self.describe_changes_locator, text)
        
    def click_modal_submit_changes_button(self):
        self.click(self.submit_changes_button_locator, True, self.timeout)


class KnowledgeBaseShowHistory(KnowledgeBase):
    
    page_title = 'Revision History'
    
    delete_document_link_locator = "css=div#delete-doc > a[href*='delete']"
    delete_confirmation_btn_locator = "css=input[value='Delete']"

    #history of the test
    top_revision_comment= "css=ul > li:nth-child(2) > div.comment"

    def delete_entire_article_document(self):
        self.click_delete_entire_article_document()
        self.click_delete_confirmation_button()

    def click_delete_entire_article_document(self):
        self.click(self.delete_document_link_locator, True, self.timeout)

    def click_delete_confirmation_button(self):
        self.click(self.delete_confirmation_btn_locator, True, self.timeout)

    @property
    def most_recent_revision_comment(self):
        return self.get_text(self.top_revision_comment)