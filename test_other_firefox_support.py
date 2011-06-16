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
import pytest

import other_support_page


class TestOtherSupport:

    @pytest.mark.fft
    @pytest.mark.prod
    def test_other_support_page(self, testsetup):
        other_support_page_obj = other_support_page.OtherSupportPage(testsetup)

        other_support_page_obj.go_to_other_support_page()
        assert other_support_page_obj.is_element_present(other_support_page_obj.moz_community_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.moz_zine_forum_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.faq_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.win_bbs_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.netscape_faq_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.silly_dog_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.tbird_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.moz_news_link)
        assert other_support_page_obj.is_text_present(other_support_page_obj.alt_fan_text)
        assert other_support_page_obj.is_element_present(other_support_page_obj.irc_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.chatzilla_link)
        assert other_support_page_obj.is_element_present(other_support_page_obj.fx_channel_link)
