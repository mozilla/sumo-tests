# -*- coding: utf-8 -*-
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
import pytest

import search_page


class TestSearchUnknownchars:

    @pytest.mark.smoketests
    @pytest.mark.prod
    @pytest.mark.bft
    @pytest.mark.fft
    def test_search_unknownchars(self, testsetup):
        search_pg = search_page.SearchPage(testsetup)

        # We're checking to ensure that
        # "unknown" characters like
        #  "�" don't appear
        search_pg.open(
        "/search?where=all&locale=ja&q=%E3%83%96%E3%83%83%E3%82%AF%E3%83%9E" +
        "%E3%83%BC%E3%82%AF%E3%81%AE%E6%95%B4%E7%90%86&sa")
        assert search_pg.is_text_present(u"ブックマークの整理")
        assert not(search_pg.is_text_present(u"�"))
