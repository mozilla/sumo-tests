import time

import pytest

import sumo_page

class TestAnonAdvPaginationNumericLinks:

    @pytest.mark.smoketests
    @pytest.mark.bft
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
