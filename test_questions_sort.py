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
import pytest

import questions_page


class TestQuestionsSort:

    @pytest.mark.fft
    @pytest.mark.prod
    def test_that_questions_sorts_correctly_by_filter_equal_to_solved(self, testsetup):
        """
           Goes to the /questions page,
           Verifies the sort filter=solved works
        """
        questions_pg = questions_page.QuestionsPage(testsetup)
        expected_sorted_text = "Solved"

        questions_pg.go_to_forum_questions_page()
        questions_pg.click_sort_by_solved_questions()
        # if there are no questions in the list then skip the test
        if not questions_pg.are_questions_present():
            pytest.skip("No questions present for filter=%s" % expected_sorted_text)
        num_of_questions = questions_pg.get_questions_count

        for counter in range(num_of_questions):
            actual_sorted_text = questions_pg.get_sorted_list_filter_text(counter + 1)
            assert actual_sorted_text == expected_sorted_text,\
                   "Expected Sorted Reply text : %s Actual Text: %s" % (expected_sorted_text, actual_sorted_text)

    @pytest.mark.fft
    @pytest.mark.prod
    def test_that_questions_sorts_correctly_by_filter_equal_to_no_replies(self, testsetup):
        """
           Goes to the /questions page,
           Verifies the sort filter=noreplies works
        """
        questions_pg = questions_page.QuestionsPage(testsetup)
        expected_sorted_text = "No replies"

        questions_pg.go_to_forum_questions_page()
        questions_pg.click_sort_by_no_replies_questions()
        # if there are no questions in the list then skip the test
        if not questions_pg.are_questions_present():
            pytest.skip("No questions present for filter=%s" % expected_sorted_text)
        num_of_questions = questions_pg.get_questions_count

        for counter in range(num_of_questions):
            index = counter + 1
            actual_sorted_text = questions_pg.get_sorted_list_filter_text(index)
            assert actual_sorted_text == expected_sorted_text,\
                   "Expected Sorted Reply text : %s Actual Text: %s" % (expected_sorted_text, actual_sorted_text)
