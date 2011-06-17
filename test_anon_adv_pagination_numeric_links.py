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
import time

import pytest

import sumo_page

class TestAnonAdvPaginationNumericLinks:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    @pytest.mark.prod
    def test_anon_adv_pagination_numeric_links(self,testsetup):
        sel = testsetup.selenium
        sumo_page_obj = sumo_page.SumoPage(testsetup)
        # This testcase checks the follwoing about pagination links
        # a)the current page is not a link
        # b)All the other page links are active
        next = "Next"
        # Do a search for which many hits are expected...
        #sel.type("fsearch-new", "\"bookmarks\"")
        #let's pick a word with fewer results...
        sumo_page_obj.open("/en-US/search?a=2")
        #sumo_func.open(sel,"en-US/search?a=2" )
        search_word = "bookmarks"
        sel.type("kb_q", search_word)
        sumo_page_obj.click("css=input[value='Search']",True, testsetup.timeout)
        not_found = True
        counter = 1
        while(not_found and counter < 5):
            if(not(sel.is_text_present(search_word))):
                sel.refresh()
                sel.wait_for_page_to_load(testsetup.timeout)
                time.sleep(2)
                counter = counter+1
            else:
                not_found = False
        pageCounter = 1
        # Using JS,get and store the last link
        li_count = int(sel.get_xpath_count("//div[@id='content-inner']/div[3]/ol[2]/li"))
        lastLink = (li_count - 1)
        #lastLink = int(sel.get_text("css=ol.pagination > li:nth-child(10)"))
        # Iterate over every page of hits....
        # Verify that current page number is NOT active....
        #self.failIf(sel.is_element_present("link=" + pageCounter))
        #except AssertionError, e: self.verificationErrors.append(str(e))
        while (sel.is_element_present("link=" + next) and
               int(pageCounter) + 1 <= int(lastLink) - 3):
            # Verify that all page numbers previous to current page ARE active
            linkNumber = 1
            while int(linkNumber) < int(pageCounter):
                if int(linkNumber) < int(pageCounter) - 3:
                    linkNumber = linkNumber + 1
                    continue
                self.failUnless(
                sel.is_element_present("link=" + str(linkNumber)),
                "Link for page %s not found" % str(linkNumber))
                linkNumber = linkNumber + 1
            # Verify that all page numbers following current page ARE active
            linkNumber = int(pageCounter) + 1
            while int(linkNumber) <= int(pageCounter) + 3:
                self.failUnless(
                sel.is_element_present("link=" + str(linkNumber)),
                "Link for page %s not found" % str(linkNumber))
                linkNumber = linkNumber + 1
            # Exit the loop immediately IFF there's no "Next" link to click on!
            pageCounter = int(pageCounter) + 1
            sumo_page_obj.click("link=" + next, True, testsetup.timeout)
