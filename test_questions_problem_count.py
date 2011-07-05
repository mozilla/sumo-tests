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
import random

import pytest

import questions_page


class TestQuestionProbCount:

    thread_loc = ''
    thread_num = str(random.randint(100, 10000))
    thread_title = 'test_thread_' + thread_num
    thread_text = 'some text'

    @pytest.mark.bft
    @pytest.mark.fft
    def test_that_questions_problem_count_increments(self, testsetup):
        """Checks if the 'I have this problem too' counter increments"""
        questions_page_obj = questions_page.QuestionsPage(testsetup)

        #   click on a question from the list of 20 questions
        #   If a question does not have 'I have this problem too'
        #   button then keep clicking through the list until you find one

        found = False
        counter = 0
        while not found and counter < 20:
            num = random.randint(1, 20)
            questions_page_obj.go_to_forum_questions_page()
            questions_page_obj.click_any_question(num)
            if questions_page_obj.is_element_present(\
               questions_page_obj.problem_too_button):
                found = True
            counter += 1

        if not found and counter == 20:
            return

        initial_count = questions_page_obj.get_problem_count
        questions_page_obj.click_problem_too_button()
        questions_page_obj.refresh()
        post_click_count = questions_page_obj.get_problem_count

        assert (initial_count + 1) == post_click_count
