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

import ask_new_questions_page
import sumo_page


class QuestionsPage(sumo_page.SumoPage):
    """
    'Ask a Question' page.
    """
    _page_title                   = 'Firefox Support Forum'
    _forums_page_url               = '/en-US/questions'
    _ask_question_link             = '/en-US/questions/new'
    _question_list_link            = "css=ol.questions > li:nth-child(%d) > div:nth-child(1) > h2 > a"
    _problem_too_button            = "css=input[value*='problem']"
    _no_thanks_link                = "link=*No*Thanks*"
    _problem_count_text            = "css=div[class^='have-problem'] > mark"
    _sort_solved_link             = "css=a[href*=filter=solved]"
    _sort_unsolved_link           = "css=a[href*=filter=unsolved]"
    _sort_no_replies_link         = "css=a[href*=filter=no-replies]"
    _solved_or_unsolved_text      = "css=ol.questions > li:nth-child(%s) > div.thread-meta > span"
    _questions_list_block         = "css=ol.questions"
    _questions_list_xpath         = "//ol[@class='questions']/li"

    @property
    def problem_too_button(self):
        return self._problem_too_button

    def go_to_forum_questions_page(self):
        self.open(self._forums_page_url)
        self.is_the_current_page

    def click_ask_new_questions_link(self):
        self.click(self._ask_question_link, True, self.timeout)
        ask_new_questions_pg = ask_new_questions_page.AskNewQuestionsPage(self.testsetup)
        return ask_new_questions_pg

    def go_to_thread(self, url):
        self.selenium.open(url)

    def click_any_question(self, num):
        q_link = self._question_list_link % num
        self.selenium.click(q_link)
        self.selenium.wait_for_page_to_load(self.timeout)

    def click_problem_too_button(self):
        self.selenium.click(self._problem_too_button)
        self.wait_for_element_present(self._no_thanks_link)

    def get_problem_count(self):
        count_text = self.selenium.get_text(self._problem_count_text)
        count_text = count_text.split()
        count = int(count_text[0])
        return count

    def click_sort_by_solved_questions(self):
        self.click(self._sort_solved_link, True, self.timeout)

    def click_sort_by_unsolved_questions(self):
        self.click(self._sort_unsolved_link, True, self.timeout)

    def click_sort_by_no_replies_questions(self):
        self.click(self._sort_no_replies_link, True, self.timeout)

    def are_questions_present(self):
        if self.selenium.is_element_present(self._questions_list_block):
            return True
        else:
            return False

    def get_questions_count(self):
        return self.selenium.get_xpath_count(self._questions_list_xpath)

    def get_sorted_list_filter_text(self, question_number):
        locator = self._solved_or_unsolved_text % question_number
        return self.selenium.get_text(locator)
