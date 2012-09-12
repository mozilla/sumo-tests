#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import datetime
from unittestzero import Assert

from pages.desktop.page_provider import PageProvider


class TestQuestions:

    @pytest.mark.native
    def test_that_posting_question_works(self, mozwebqa):
        """Posts a question to /questions"""
        timestamp = datetime.datetime.today()
        q_to_ask = "automation test question %s" % (timestamp)
        q_details = "This is a test. %s" % (timestamp)

        # go to the /questions/new page and log in
        ask_new_questions_page = PageProvider(mozwebqa).new_question_page()

        # post a question
        ask_new_questions_page.click_firefox_product_link()
        ask_new_questions_page.click_category_problem_link()
        ask_new_questions_page.type_question(q_to_ask)
        ask_new_questions_page.click_none_of_these_solve_my_problem_button()
        view_question_pg = ask_new_questions_page.fill_up_questions_form(q_to_ask, q_details)

        Assert.equal(view_question_pg.question, q_to_ask)
        Assert.equal(view_question_pg.question_detail, q_details)

    @pytest.mark.nondestructive
    def test_that_questions_sorts_correctly_by_filter_equal_to_solved(self, mozwebqa):
        """
           Goes to the /questions page,
           Verifies the sort filter=solved works
        """
        expected_sorted_text = "SOLVED"

        questions_page = PageProvider(mozwebqa).questions_page()
        questions_page.click_to_expand_sort_and_filter_box()
        Assert.true(questions_page.is_sort_and_filter_box_expanded)

        questions_page.click_sort_by_solved_questions()
        # if there are no questions in the list then skip the test
        if not questions_page.are_questions_present:
            pytest.skip("No questions present for filter=%s" % expected_sorted_text)

        for question in questions_page.questions:
            actual_sorted_text = question.sorted_list_filter_text
            Assert.equal(actual_sorted_text, expected_sorted_text)

    @pytest.mark.nondestructive
    def test_that_questions_sorts_correctly_by_filter_equal_to_no_replies(self, mozwebqa):
        """
           Goes to the /questions page,
           Verifies the sort filter=noreplies works
        """
        expected_sorted_text = "No replies"

        questions_page = PageProvider(mozwebqa).questions_page()
        questions_page.click_to_expand_sort_and_filter_box()
        Assert.true(questions_page.is_sort_and_filter_box_expanded)

        questions_page.click_sort_by_no_replies_questions()
        # if there are no questions in the list then skip the test
        if not questions_page.are_questions_present:
            pytest.skip("No questions present for filter=%s" % expected_sorted_text)

        for question in questions_page.questions:
            Assert.equal(0, question.number_of_replies)

    @pytest.mark.xfail(reason="Bug 790599 - [stage] After clicking 'I have this problem too' the counter interments the total number by 5 instead of 1")
    def test_that_questions_problem_count_increments(self, mozwebqa):
        """Checks if the 'I have this problem too' counter increments"""

        # Can't +1 your own question so will do it logged out
        questions_page = PageProvider(mozwebqa).questions_page()
        view_question_page = questions_page.click_any_question(1)

        initial_count = view_question_page.problem_count
        view_question_page.click_problem_too_button()
        view_question_page.refresh()
        post_click_count = view_question_page.problem_count

        Assert.equal(initial_count + 1, post_click_count)
