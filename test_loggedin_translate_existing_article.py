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
#                 Zac Campbell
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

#import pytest
import datetime
from login_page import LoginPage
from support_home_page import SupportHomePage
from knowledge_base_article import KnowledgeBaseArticle
from knowledge_base_translate import KnowledgeBaseTranslate
from unittestzero import Assert

class TestLoggedInTranslateExistingArticle():

    #def setUp(self):
    #    self.selenium = selenium(
    #    vars.ConnectionParameters.server,
    #    vars.ConnectionParameters.port,
    #    vars.ConnectionParameters.browser,
    #    vars.ConnectionParameters.baseurl)
    #    self.selenium.start()
    #    self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)
    #    self.accounts = sumo_test_data.SUMOtestData()
    #    self.functions = sumo_functions.SUMOfunctions()

    def test_loggedin_translate_existing_article(self, mozwebqa):
        login_po = LoginPage(mozwebqa)
        home_po = SupportHomePage(mozwebqa)
        kb_article_po = KnowledgeBaseArticle(mozwebqa)
        kb_translate_po = KnowledgeBaseTranslate(mozwebqa)
        timestamp = datetime.datetime.now()
        
        login_po.log_in('default')
        
        home_po.click_top_common_content_link()
        
        kb_article_po.click_translate_article()
        
        kb_translate_po.click_translate_language("Esperanto (eo)")
        
        kb_translate_po.type_title("article_title_%s" % timestamp)
        kb_translate_po.type_slug("article_slug_%s" % timestamp)
        
        kb_translate_po.click_submit_review()
        
        kb_translate_po.type_modal_describe_changes("article_changes_%s" % timestamp)
        kb_translate_po.click_modal_submit_changes_button()
        
        print timestamp.time()
        print kb_translate_po.most_recent_revision_date
        rev_date = datetime.datetime.strptime(kb_translate_po.most_recent_revision_date, "%Y-%m-%dT%H:%M:%S")
        print rev_date.time()
        
        Assert.true(rev_date > timestamp, "%s not greater than %s" % (rev_date.date(), timestamp.date()))
        
        
#
#    def test_loggedin_translate_existing_article(self):
#        sel = self.selenium
#        sumo_func = sumo_functions.SUMOfunctions()
#        user = self.accounts.getUserInfo(0)
#        sumo_func.open(sel, vars.ConnectionParameters.authurl)
#        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
#        timestamp = sel.get_eval("new Date().getTime()")
#        language = "hi-IN"
#        self.functions.login(sel, 'default')
#        sumo_func.open(sel, vars.ConnectionParameters.authurlssl)
#        sel.click("css=div#mostpopular-new > ul > li:nth-child(6) > a")
#        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
#        sel.click("link=Translate this page")
#        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
#        # Selecting a language from drop-down list
#        #breaks in IE for all types of selectors
#        #sel.select("lang", "index=0")
#        sel.type("page", "article_" + timestamp)
#        sel.click("css=input[value='Create translation']")
#        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
#        sel.type("editwiki", "article_" + timestamp)
#        sel.type("comment", "article_" + timestamp)
#        sel.click("save")
#        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
#        sumo_func.open(sel, "/en-US/kb/article_" + timestamp + "?bl=n")
#        # Logging out
#        sel.click("link=Log Out")
#        sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
#        sumo_func.open(sel, "/en-US/kb/")
#
#    def tearDown(self):
#        self.selenium.stop()
#
#if __name__ == "__main__":
#    unittest.main()
