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

from login_page import LoginPage
from support_home_page import SupportHomePage
from knowledge_base_article import KnowledgeBaseArticle
from knowledge_base_translate import KnowledgeBaseTranslate
from unittestzero import Assert
import pytest

class TestLoggedInTranslateExistingArticle():

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    def test_loggedin_translate_existing_article(self, mozwebqa):
        login_po = LoginPage(mozwebqa)
        home_po = SupportHomePage(mozwebqa)
        kb_article_po = KnowledgeBaseArticle(mozwebqa)
        kb_translate_po = KnowledgeBaseTranslate(mozwebqa)
        
        login_po.log_in('default')
        
        home_po.click_top_common_content_link()
        
        kb_article_po.click_translate_article()
        kb_translate_po.click_translate_language("Esperanto (eo)")
        
        kb_translate_po.type_title("article_title_%s" % timestamp)
        kb_translate_po.type_slug("article_slug_%s" % timestamp)
        kb_translate_po.click_submit_review()
        
        change_comment = "article_changes %s" % timestamp
        kb_translate_po.type_modal_describe_changes(change_comment)
        kb_translate_po.click_modal_submit_changes_button()
        
        Assert.equal(change_comment, kb_translate_po.most_recent_revision_comment)
