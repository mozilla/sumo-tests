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
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
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
'''
Created on Aug 11, 2010

@author: mozilla
'''

import sumo_page
import vars

pageLoadTimeout = vars.ConnectionParameters.page_load_timeout

class ContributePage(sumo_page.SumoPage):
    """
    The 'How to Contribute' Page contains 
    web elements and methods that can be 
    performed on them. This page is a kb article that
    educated users/contributors how to get started.
    """
    _page_title            = 'How to contribute'
    page_url               = '/en-US/kb/How+to+contribute'
    
    improve_kb_link        = "css=a[href *= 'Contributing+to+the+Knowledge+Base']"
    translate_link         = "css=a[href *= 'Translating+articles']"
    forum_support_link     = "css=a[href *= 'Providing+Forum+Support']"
    live_chat_link         = "css=a[href *= 'Helping+with+Live+Chat']"
    stay_in_contact_link   = "css=a[href *= 'Stay_connected']"
    
    
    def __init__(self, selenium):
        super(ContributePage, self).__init__(selenium)               
           
    def go_to_contribute_page(self):
        self.open(self.page_url)
        self.is_the_current_page
        

        
