#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import datetime
from unittestzero import Assert
from random import randrange
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
        ask_new_questions_page.close_stage_site_banner()
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

    def test_contributor_flow_to_support_forum_post(self, mozwebqa):
        """
            Shows a contributor can start on the home page and move
            all the way to answering a question in the forum.
        """
        num_questions_to_display = 20
        reply_text = "reply"

        #1. Start on the home page
        #2. Log in
        #3. Use the contributor bar to go to the forums.
        #   The questions page should list 20 posts.
        #3.1 go to the question page
        question_page = PageProvider(mozwebqa).questions_page(do_login=True)
        #3.2 ensure the size of the list is 20
        Assert.equal(question_page.questions_count, num_questions_to_display,
                     'amount of displayed questions is not equal to expected value')

        #4. Click on a question. (URL is in the forum of /questions/[some number])
        #4.1 pick up an arbitrary question and click
        #4.2 check if it landed on an intended forum page
        question = question_page.questions[randrange(num_questions_to_display)]
        forum_page = question.click_question_link()

        #5. Go to the thread
        #6. Scroll to the bottom and click into the text field
        #7. Type reply
        #7.1 get the login-user name to check the author of the reply
        username = forum_page.header.login_user_name
        #7.2 reply the post
        forum_page.post_reply(reply_text)
        #7.3 check if posting a reply finishes without an error
        is_reply_present, post_author_name = forum_page.is_reply_text_present(username, reply_text)
        Assert.true(is_reply_present, 
            u'reply with "%s" text posted by %s (actually: %s) is not present' % (reply_text, username, post_author_name))
