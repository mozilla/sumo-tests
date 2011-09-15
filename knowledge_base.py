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

from sumo_page import SumoPage


class KnowledgeBase(SumoPage):
    
    @property
    def navigaton(self):
        return self.Navigation(self.testsetup)
    
    class Navigation(SumoPage):
        
        article_locator = "link=Article"
        edit_article_locator = "link=Edit Article"
        translate_article_locator = "link=Translate Article"
        show_history_locator = "link=Show History"
        
        def click_article(self):
            self.click(self.article_locator, True, self.timeout)
        
        def click_edit_article(self):
            self.click(self.edit_article_locator, True, self.timeout)
        
        def click_translate_article(self):
            self.click(self.translate_article_locator, True, self.timeout)
        
        def click_show_history(self):
            self.click(self.show_history_locator, True, self.timeout)