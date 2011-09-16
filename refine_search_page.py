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
'''
Created on Jun 30, 2010

@author: mozilla
'''
from sumo_page import SumoPage

class RefineSearchPage(SumoPage):
    """
       'Advanced Search' page. 
    """
    page_title = 'Search'
    page_url = '/en-US/search?a=2'
    article_search_box = "kb_q"
    post_search_box = 'support_q'
    post_tags_box = 'id_q_tags'
    thread_search_box = 'discussion_q'
    search_button_kb = "css=input[name='w'][value='1']+div.submit-search > input[type='submit']"
    search_button_support = "css=input[name='w'][value='2']+div.submit-search > input[type='submit']"
    search_button_disc = "css=input[name='w'][value='4']+div.submit-search > input[type='submit']"
    kb_cat_check_box = "css=input#id_category_0"
    kb_tab = "css=div#search-tabs > ul > li:nth-child(1) > a"
    support_questions_tab = "css=div#search-tabs > ul > li:nth-child(2) > a"
    forums_tab = "css=div#search-tabs > ul > li:nth-child(3) > a"             
    asked_by_box = "id_asked_by"
    search_results_list = "css=div.result.question"
 
    def go_to_refine_search_page(self):
        self.open(self.page_url)
        self.is_the_current_page

    def click_support_questions_tab(self):
        self.click(self.support_questions_tab) 

    def type_in_asked_by_box(self, text):
        self.type(self.asked_by_box, text)

    def click_search_button_support(self):
        self.click(self.search_button_support, True)

    def do_search_on_knowledge_base(self, search_query, search_page_obj):
        self.click(self.kb_tab)
        self.type(self.article_search_box, search_query)
        self.click(self.search_button_kb, True)
        search_page_obj.is_the_current_page

    def do_search_on_support_questions(self, search_query, search_page_obj):
        self.click(self.support_questions_tab)
        self.type(self.post_search_box, search_query)
        self.click(self.search_button_support, True)
        search_page_obj.is_the_current_page

    def do_search_tags_on_support_questions(self, search_query, search_page_obj):
        self.click(self.support_questions_tab)
        self.type(self.post_tags_box, search_query)
        self.click(self.search_button_support, True)
        search_page_obj.is_the_current_page

    def do_search_on_discussion_forums(self, search_query, search_page_obj):
        self.click(self.forums_tab)
        self.type(self.thread_search_box, search_query)
        self.click(self.search_button_disc, True)
        search_page_obj.is_the_current_page

    def is_kb_cat_checked(self):
        return self.selenium.is_checked(self.kb_cat_check_box)
    
    @property
    def search_result_count(self):
        return self.selenium.get_css_count(self.search_results_list)
        