#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
from pages.desktop.page_provider import PageProvider
import datetime
import pytest


class TestQuestions:

    def test_that_posting_question_works(self, mozwebqa):
        """Posts a question to /questions"""
        timestamp = datetime.datetime.today()
        q_to_ask = "automation test question %s" % (timestamp)
        q_details = "This is a test. %s" % (timestamp)

        # go to the /questions/new page and log in
        ask_new_questions_pg = PageProvider(mozwebqa).new_question_page()

        # post a question
        ask_new_questions_pg.click_firefox_product_link()
        ask_new_questions_pg.click_category_problem_link()
        ask_new_questions_pg.type_question(q_to_ask)
        ask_new_questions_pg.click_provide_details_button()
        view_question_pg = ask_new_questions_pg.fill_up_questions_form(q_to_ask, q_details)

        Assert.equal(view_question_pg.question, q_to_ask)
        Assert.equal(view_question_pg.question_detail, q_details)

        # sign out
        ask_new_questions_pg.sign_out()

    @pytest.mark.nondestructive
    def test_that_questions_sorts_correctly_by_filter_equal_to_solved(self, mozwebqa):
        """
           Goes to the /questions page,
           Verifies the sort filter=solved works
        """
        expected_sorted_text = "Solved"

        questions_pg = PageProvider(mozwebqa).questions_page()
        questions_pg.click_sort_by_solved_questions()
        # if there are no questions in the list then skip the test
        if not questions_pg.are_questions_present:
            pytest.skip("No questions present for filter=%s" % expected_sorted_text)
        num_of_questions = questions_pg.questions_count

        for counter in range(num_of_questions):
            actual_sorted_text = questions_pg.sorted_list_filter_text(counter + 1)
            Assert.equal(actual_sorted_text, expected_sorted_text)

    @pytest.mark.nondestructive
    def test_that_questions_sorts_correctly_by_filter_equal_to_no_replies(self, mozwebqa):
        """
           Goes to the /questions page,
           Verifies the sort filter=noreplies works
        """
        expected_sorted_text = "No replies"

        questions_pg = PageProvider(mozwebqa).questions_page()
        questions_pg.click_sort_by_no_replies_questions()
        # if there are no questions in the list then skip the test
        if not questions_pg.are_questions_present:
            pytest.skip("No questions present for filter=%s" % expected_sorted_text)
        num_of_questions = questions_pg.questions_count

        for counter in range(num_of_questions):
            index = counter + 1
            actual_sorted_text = questions_pg.sorted_list_filter_text(index)
            Assert.equal(actual_sorted_text, expected_sorted_text)

    def test_that_questions_problem_count_increments(self, mozwebqa):
        """Checks if the 'I have this problem too' counter increments"""

        # Can't +1 your own question so will do it logged out
        questions_pg = PageProvider(mozwebqa).questions_page()
        view_question_pg = questions_pg.click_any_question(1)

        initial_count = view_question_pg.problem_count
        view_question_pg.click_problem_too_button()
        view_question_pg.refresh()
        post_click_count = view_question_pg.problem_count

        Assert.greater(post_click_count, initial_count)
