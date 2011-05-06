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
# Contributor(s): Tanay G.
#                 Vishal K.
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

import unittest
import datetime

from selenium import selenium

import questions_page
import login_page
import sumo_test_data
import vars

class TestAAQ(unittest.TestCase):
    
    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

                
    def test_that_posting_question_works(self):
        """Posts a question to /questions"""
        login_po            = login_page.LoginPage(self.selenium)
        questions_po        = questions_page.QuestionsPage(self.selenium)
        timestamp           = self.selenium.get_eval("new Date().getTime()")
        q_to_ask            = "automation test question %s" %(datetime.date.today())
        q_details           = "This is a test. " + timestamp


        user_info       = sumo_test_data.SUMOtestData().getUserInfo(0)
        uname           = user_info['username']
        pwd             = user_info['password']
        
        ''' login '''
        login_po.log_in(uname, pwd)
        
        """ go to the /questions/new page and post a question
        """
        questions_po.go_to_ask_new_questions_page()
        questions_po.click_firefox_product_link()
        questions_po.click_category_problem_link()
        questions_po.type_question(q_to_ask)
        questions_po.click_provide_details_button()
        questions_po.fill_up_questions_form(q_details)
        
        self.failUnless(self.selenium.is_text_present(q_to_ask))
        self.failUnless(self.selenium.is_text_present(q_details))
        
if __name__ == "__main__":
    unittest.main()                                               