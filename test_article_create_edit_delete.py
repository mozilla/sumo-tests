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
import re
import random

import unittest
from selenium import selenium

import vars
import sumo_test_data
import knowledge_base_page
import login_page

class TestArticleCreateEditDelete(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
                                 vars.ConnectionParameters.server,
                                 vars.ConnectionParameters.port,
                                 vars.ConnectionParameters.browser,
                                 vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()
        
    def test_article_creating_editing_deleting(self):
        """
           Creates a new knowledge base article,
           edits it and deletes it. Verifies creation,
           edition & deletion
        """
        sel = self.selenium
        kb_pg = knowledge_base_page.KBPage(sel)
        login_pg = login_page.LoginPage(sel)

        #login with an Admin account as he can delete the article
        
        user_info = sumo_test_data.SUMOtestData().getUserInfo(1)
        uname = user_info['username']
        pwd   = user_info['password']
        
        login_pg.log_in(uname, pwd)
 
        random_num = random.randint(1000, 9999)
        article_name = str("test_article_%s" %(random_num))
        
        article_info_dict = {'title':article_name,'category':'How to','keyword':'test',
                             'summary':"this is an automated summary_"+str(random_num),
                             'content':"automated content_"+str(random_num)}
        
        # create a new article
        kb_pg.go_to_create_new_article_page()
        kb_pg.create_or_edit_article(article_info_dict)
        
        
        # verify article history
        article_history_url = kb_pg.get_url_current_page()
        kb_pg.open(article_history_url)
        self.verify_article_history(kb_pg, article_history_url, article_name)
        
        # verify article contents
        article_url = article_history_url.replace("/history","")
        kb_pg.open(article_url)
        kb_pg.click_edit_article()

        kb_pg.is_text_present(article_info_dict['title'])
        actual_summary_text = kb_pg.get_article_summary_text()
        actual_contents_text = kb_pg.get_article_contents_box()
        assert article_info_dict['summary'] == actual_summary_text,\
               "Expected: %s Actual: %s" %(article_info_dict['summary'], actual_summary_text)
        assert article_info_dict['content'] == actual_contents_text,\
               "Expected: %s Actual: %s" %(article_info_dict['content'], actual_contents_text)
        
        # edit that same article
        article_info_dict_edited = {'title':article_name+"_edited",
                                    'category':'How to','keyword':'test',
                                    'summary':"this is an automated summary_"+str(random_num)+"_edited",
                                    'content':"automated content_"+str(random_num)+"_edited"}
        kb_pg.create_or_edit_article(article_info_dict_edited)
        kb_pg.open(article_url)
        kb_pg.click_edit_article()

        kb_pg.is_text_present(article_info_dict_edited['title'])
        actual_summary_text = kb_pg.get_article_summary_text()
        actual_contents_text = kb_pg.get_article_contents_box()
        assert article_info_dict_edited['summary'] == actual_summary_text,\
               "Expected: %s Actual: %s" %(article_info_dict_edited['summary'], actual_summary_text)
        assert article_info_dict_edited['content'] == actual_contents_text,\
               "Expected: %s Actual: %s" %(article_info_dict_edited['content'], actual_contents_text)
        
        # delete the same article
        kb_pg.open(article_history_url)
        kb_pg.click_delete_entire_article_document()
        kb_pg.click_delete_confirmation_button()
        assert kb_pg.is_text_present('document has been deleted'),\
               "Delete confirmation text not present"
               
    def verify_article_history(self, kb_pg, article_history_url, article_name):
        actual_page_title = kb_pg.selenium.get_title()
        if re.search(article_name, actual_page_title, re.IGNORECASE) is None:
            kb_pg.open(article_history_url)
        
        if not (kb_pg.page_title_revision_history in actual_page_title):
            raise Exception("Expected string: %s not found in title: %s" %(kb_pg.page_title_revision_history,actual_page_title))

if __name__ == "__main__":
    unittest.main()
