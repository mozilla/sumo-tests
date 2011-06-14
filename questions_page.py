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

import time
import re

import sumo_page

class QuestionsPage(sumo_page.SumoPage):
    """
    'Ask a Question' page.
    """
    _page_title                   = 'Firefox Support Forum'
    _page_title_questions_new     = 'Ask a Question'
    forums_page_url               = '/en-US/questions'
    questions_new_url             = '/en-US/questions/new'
    ask_question_link             = '/en-US/questions/new'
    firefox_product_first_link    = 'css=ul.select-one > li > a'
    category_prob_first_link      = 'css=ul.select-one > li > a'
    type_question_box             = 'search'
    ask_this_button               = "css=input[value='Ask this']"
    none_of_these_button          = "css=input[value *='None']"
    question_list_link            = "css=ol.questions > li:nth-child(%d) > div:nth-child(1) > h2 > a"
    problem_too_button            = "css=input[value*='problem']"
    no_thanks_link                = "link=*No*Thanks*"
    problem_count_text            = "css=div[class^='have-problem'] > mark"
    provide_details_button        = "show-form-btn"
    q_content_box                 = 'id_content'
    q_site_box                    = 'id_sites_affected'
    q_trouble_box                 = 'id_troubleshooting'
    q_post_button                 = "css=input[value='Post Question']"

    def go_to_forum_questions_page(self):
        self.open(self.forums_page_url)
        self.is_the_current_page
        
    def go_to_ask_new_questions_page(self):
        self.selenium.open(self.questions_new_url)
        if (re.search(self._page_title_questions_new, self.selenium.get_title()) is None):
            raise Exception, '\r\nPage title verification failed. Expected: %s; Actual:%s\r\n'\
                              % (self._page_title_questions_new,self.selenium.get_title())

    def click_ask_new_questions_link(self):
        self.click(self.ask_question_link, True, self.timeout)
        
    def click_firefox_product_link(self):
        self.click(self.firefox_product_first_link, True, self.timeout)
        
    def click_category_problem_link(self):
        self.click(self.category_prob_first_link, True, self.timeout)
        
    def type_question(self, question_to_ask):
        self.type(self.type_question_box, question_to_ask)
        self.click(self.ask_this_button, True, self.timeout)
          
    def go_to_thread(self,url):
        self.selenium.open(url)
        
    def click_any_question(self, num):
        q_link = self.question_list_link % num
        self.selenium.click(q_link)
        self.selenium.wait_for_page_to_load(self.timeout)
        
    def click_problem_too_button(self):
        self.selenium.click(self.problem_too_button)
        time.sleep(2)
        
    def click_provide_details_button(self):
        self.click(self.provide_details_button, True, self.timeout)
        
    def fill_up_questions_form(self, q_text='details', q_site='www.example.com', q_trouble='no addons'):
        self.type(self.q_content_box, q_text)
        self.type(self.q_site_box, q_site)
        self.type(self.q_trouble_box, q_trouble)
        self.click(self.q_post_button, True, self.timeout)
         
    def get_problem_count(self):
        count_text = self.selenium.get_text(self.problem_count_text)
        count_text = count_text.split()
        count = int(count_text[0])
        return count
        
        
        
    
        
