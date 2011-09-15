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
# Contributor(s): Zac Campbell
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
from knowledge_base import KnowledgeBase


class KnowledgeBaseTranslate(KnowledgeBase):
    
    description_title_locator = "id_title"
    description_slug_locator = "id_slug"
    preview_content_button_locator = "btn-preview"
    submit_button_locator = "btn-submit"
    
    # 2 elements inside the modal popup
    describe_changes_locator = "id_comment"
    submit_changes_button_locator = "css=#submit-modal > input"
    
    #history of the test
    top_revision_comment= "css=ul > li:nth-child(2) > div.comment"
    
    def click_translate_language(self, language):
        self.click("link=%s" % language, True, self.timeout)
    
    def type_title(self, text):
        self.type(self.description_title_locator, text)
    
    def type_slug(self, text):
        self.type(self.description_slug_locator, text)
        
    def click_submit_review(self):
        self.click(self.submit_button_locator)
        
    def type_modal_describe_changes(self, text):
        self.type(self.describe_changes_locator, text)
        
    def click_modal_submit_changes_button(self):
        self.click(self.submit_changes_button_locator, True, self.timeout)

    @property
    def most_recent_revision_comment(self):
        return self.get_text(self.top_revision_comment)
