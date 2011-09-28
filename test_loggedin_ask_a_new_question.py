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
# Tanay G.
# Portions created by the Initial Developer are Copyright (C) 2___
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Tanay
#                 Vishal
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
from unittestzero import Assert
from questions_page import ViewQuestionPage
from questions_page import AskNewQuestionsPage
from login_page import LoginPage
import datetime
import pytest


class TestAAQ:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    def test_that_posting_question_works(self, mozwebqa):
        """Posts a question to /questions"""
        login_po = LoginPage(mozwebqa)
        ask_new_questions_pg = AskNewQuestionsPage(mozwebqa)
        view_question_pg = ViewQuestionPage(mozwebqa)
        timestamp = datetime.datetime.today()
        q_to_ask = "automation test question %s" % (timestamp)
        q_details = "This is a test. %s" % (timestamp)

        login_po.log_in('default')

        # go to the /questions/new page and post a question
        ask_new_questions_pg.go_to_ask_new_questions_page()
        ask_new_questions_pg.click_firefox_product_link()
        ask_new_questions_pg.click_category_problem_link()
        ask_new_questions_pg.type_question(q_to_ask)
        ask_new_questions_pg.click_provide_details_button()
        ask_new_questions_pg.fill_up_questions_form(q_details)

        Assert.equal(view_question_pg.question, q_to_ask)
        Assert.equal(view_question_pg.question_detail, q_details)
