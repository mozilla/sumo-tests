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
from sumo_page import SumoPage
from questions_page import ViewQuestionPage


class AskNewQuestionsPage(SumoPage):
    """
    'Ask a New Question' page.
    Child class of Questions Page
    """
    page_title                            = 'Ask a Question'
    questions_new_url                     = '/en-US/questions/new'
    firefox_product_first_link_locator    = 'css=ul.select-one > li > a'
    category_prob_first_link_locator      = 'css=ul.select-one > li > a'
    type_question_box_locator             = 'search'
    ask_this_button_locator               = "css=input[value='Ask this']"
    none_of_these_button_locator          = "css=input[value *='None']"
    provide_details_button_locator        = "show-form-btn"
    q_content_box_locator                 = 'id_content'
    q_site_box_locator                    = 'id_sites_affected'
    q_trouble_box_locator                 = 'id_troubleshooting'
    q_post_button_locator                 = "css=input[value='Post Question']"
    sort_solved_link_locator              = "css=a[href*=filter=solved]"
    sort_unsolved_link_locator            = "css=a[href*=filter=unsolved]"
    sort_no_replies_link_locator          = "css=a[href*=filter=no-replies]"
    solved_or_unsolved_text_locator       = "css=ol.questions > li:nth-child(%s) > div.thread-meta > span"
    questions_list_block_locator          = "css=ol.questions"
    questions_list_xpath_locator          = "//ol[@class='questions']/li"

    def go_to_ask_new_questions_page(self):
        self.selenium.open(self.questions_new_url)
        self.is_the_current_page

    def click_firefox_product_link(self):
        self.click(self.firefox_product_first_link_locator, True, self.timeout)

    def click_category_problem_link(self):
        self.click(self.category_prob_first_link_locator, True, self.timeout)

    def type_question(self, question_to_ask):
        self.type(self.type_question_box_locator, question_to_ask)
        self.click(self.ask_this_button_locator, True, self.timeout)

    def click_provide_details_button(self):
        self.click(self.provide_details_button_locator, True, self.timeout)

    def fill_up_questions_form(self, q_text='details', q_site='www.example.com', q_trouble='no addons'):
        self.type(self.q_content_box_locator, q_text)
        self.type(self.q_site_box_locator, q_site)
        self.type(self.q_trouble_box_locator, q_trouble)
        self.click(self.q_post_button_locator, True, self.timeout)
        return ViewQuestionPage(self.testsetup)

    def get_sorted_list_filter_text(self, question_number):
        locator = self.solved_or_unsolved_text_locator % question_number
        return self.selenium.get_text(locator)