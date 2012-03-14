#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
from pages.desktop.questions_page import QuestionsPage
import pytest


class TestQuestionsSort:

    @pytest.mark.fft
    @pytest.mark.prod
    def test_that_questions_sorts_correctly_by_filter_equal_to_solved(self, mozwebqa):
        """
           Goes to the /questions page,
           Verifies the sort filter=solved works
        """
        questions_pg = QuestionsPage(mozwebqa)
        expected_sorted_text = "Solved"

        questions_pg.go_to_forum_questions_page()
        questions_pg.click_sort_by_solved_questions()
        # if there are no questions in the list then skip the test
        if not questions_pg.are_questions_present:
            pytest.skip("No questions present for filter=%s" % expected_sorted_text)
        num_of_questions = questions_pg.questions_count

        for counter in range(num_of_questions):
            actual_sorted_text = questions_pg.sorted_list_filter_text(counter + 1)
            Assert.equal(actual_sorted_text, expected_sorted_text)

    @pytest.mark.fft
    @pytest.mark.prod
    def test_that_questions_sorts_correctly_by_filter_equal_to_no_replies(self, mozwebqa):
        """
           Goes to the /questions page,
           Verifies the sort filter=noreplies works
        """
        questions_pg = QuestionsPage(mozwebqa)
        expected_sorted_text = "No replies"

        questions_pg.go_to_forum_questions_page()
        questions_pg.click_sort_by_no_replies_questions()
        # if there are no questions in the list then skip the test
        if not questions_pg.are_questions_present:
            pytest.skip("No questions present for filter=%s" % expected_sorted_text)
        num_of_questions = questions_pg.questions_count

        for counter in range(num_of_questions):
            index = counter + 1
            actual_sorted_text = questions_pg.sorted_list_filter_text(index)
            Assert.equal(actual_sorted_text, expected_sorted_text)
