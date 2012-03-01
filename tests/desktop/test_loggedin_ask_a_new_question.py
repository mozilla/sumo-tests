#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
from pages.desktop.questions_page import ViewQuestionPage
from pages.desktop.questions_page import AskNewQuestionsPage
import datetime
import pytest


class TestAAQ:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    def test_that_posting_question_works(self, mozwebqa):
        """Posts a question to /questions"""
        ask_new_questions_pg = AskNewQuestionsPage(mozwebqa)
        view_question_pg = ViewQuestionPage(mozwebqa)
        timestamp = datetime.datetime.today()
        q_to_ask = "automation test question %s" % (timestamp)
        q_details = "This is a test. %s" % (timestamp)

        # go to the /questions/new page and log in
        ask_new_questions_pg.go_to_ask_new_questions_page()
        ask_new_questions_pg.sign_in('default')

        # post a question
        ask_new_questions_pg.click_firefox_product_link()
        ask_new_questions_pg.click_category_problem_link()
        ask_new_questions_pg.type_question(q_to_ask)
        ask_new_questions_pg.click_provide_details_button()
        ask_new_questions_pg.fill_up_questions_form(q_details)

        Assert.equal(view_question_pg.question, q_to_ask)
        Assert.equal(view_question_pg.question_detail, q_details)

        # sign out
        ask_new_questions_pg.sign_out()
