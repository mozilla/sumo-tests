# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
from questions_page import ViewQuestionPage
from questions_page import QuestionsPage
import pytest


class TestQuestionProbCount:

    @pytest.mark.bft
    @pytest.mark.fft
    def test_that_questions_problem_count_increments(self, mozwebqa):
        """Checks if the 'I have this problem too' counter increments"""

        questions_pg = QuestionsPage(mozwebqa)
        view_question_pg = ViewQuestionPage(mozwebqa)

        # Can't +1 your own question so will do it logged out
        questions_pg.go_to_forum_questions_page()
        questions_pg.click_any_question(1)

        initial_count = view_question_pg.problem_count
        view_question_pg.click_problem_too_button()
        view_question_pg.refresh()
        post_click_count = view_question_pg.problem_count

        Assert.equal(initial_count + 1, post_click_count)
