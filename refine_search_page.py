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
import sumo_page

class RefineSearchPage(sumo_page.SumoPage):
    """
       'Advanced Search' page. 
    """
    _page_title                   = 'Search'
    _page_url                     = '/en-US/search?a=2'
    _article_search_box           = "kb_q"
    _post_search_box              = 'support_q'
    _post_tags_box                = 'id_q_tags'
    _thread_search_box            = 'discussion_q'
    _search_button_kb             = "css=input[name='w'][value='1']+div.submit-search > input[type='submit']"
    _search_button_support        = "css=input[name='w'][value='2']+div.submit-search > input[type='submit']"
    _search_button_disc           = "css=input[name='w'][value='4']+div.submit-search > input[type='submit']"
    _kb_cat_check_box             = "css=input#id_category_0"
    _kb_tab                       = "css=div#search-tabs > ul > li:nth-child(1) > a"
    _support_questions_tab        = "css=div#search-tabs > ul > li:nth-child(2) > a"
    _forums_tab                   = "css=div#search-tabs > ul > li:nth-child(3) > a"             
    _asked_by_box                 = "id_asked_by"

    def go_to_refine_search_page(self):
        self.open(self._page_url)
        self.is_the_current_page

    @property
    def support_questions_tab(self):
        return self._support_questions_tab

    @property
    def asked_by_box(self):
        return self._asked_by_box

    @property
    def search_button_support(self):
        return self._search_button_support

    def do_search_on_knowledge_base(self, search_query, search_page_obj):
        self.click(self._kb_tab)
        self.type(self._article_search_box, search_query)
        self.click(self._search_button_kb, True)
        search_page_obj.is_the_current_page

    def do_search_on_support_questions(self, search_query, search_page_obj):
        self.click(self._support_questions_tab)
        self.type(self._post_search_box, search_query)
        self.click(self._search_button_support, True)
        search_page_obj.is_the_current_page

    def do_search_tags_on_support_questions(self, search_query, search_page_obj):
        self.click(self._support_questions_tab)
        self.type(self._post_tags_box, search_query)
        self.click(self._search_button_support, True)
        search_page_obj.is_the_current_page

    def do_search_on_discussion_forums(self, search_query, search_page_obj):
        self.click(self._forums_tab)
        self.type(self._thread_search_box, search_query)
        self.click(self._search_button_disc, True)
        search_page_obj.is_the_current_page

    def is_kb_cat_checked(self):
        return self.selenium.is_checked(self._kb_cat_check_box)