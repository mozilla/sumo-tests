import time

import pytest

import support_home_page
import search_page

@pytest.mark.smoketests
@pytest.mark.bft
class TestAnonPaginationNumeriLinks():

    def test_anon_pagination_numeric_links(self,testsetup):   
        support_hp_obj  = support_home_page.SupportHomePage(testsetup)
        search_page_obj = search_page.SearchPage(testsetup)

        # Description:
        # This testcase checks the following about pagination links
        # a) the current page is not a link
        # b) All the other page links are active
        next = "Next"
        # Do a search for which hits are expected...
        search_word = "bookmarks"
        support_hp_obj.do_search_on_main_search_box(search_word, search_page_obj)
        not_found = True
        counter = 1
        while(not_found and counter < 5):
            if(not(testsetup.selenium.is_text_present(search_word))):
                testsetup.selenium.refresh()
                testsetup.selenium.wait_for_page_to_load(testsetup.timeout)
                time.sleep(2)
                counter = counter+1
            else:
                not_found = False
        pageCounter = 1
        # store the last link
        url = "/search?q=%s" %(search_word)
        search_page_obj.open(url)
        if(testsetup.selenium.is_element_present("css=ol.pagination > li:nth-child(7)")):
            lastLink = int(testsetup.selenium.get_text("css=ol.pagination > li:nth-child(7)"))
        else:
            return
        # Iterate over every page of hits...
        while (testsetup.selenium.is_element_present(search_page_obj.next_page_link)
               and int(pageCounter) + 1 <= int(lastLink) - 3):
            # Verify that all page numbers previous to current page ARE active
            linkNumber = 1
            while int(linkNumber) < int(pageCounter):
                if int(linkNumber) < int(pageCounter) - 3:
                    linkNumber = linkNumber + 1
                    continue
                assert(\
                      testsetup.selenium.is_element_present("link=" + str(linkNumber)),\
                      "Previous page %s is not a link" % str(linkNumber))
                linkNumber = linkNumber + 1
            # Verify that all page numbers following current page ARE active
            linkNumber = int(pageCounter) + 1
            while int(linkNumber) <= int(pageCounter) + 3:
                assert(\
                       testsetup.selenium.is_element_present("link=" + str(linkNumber)),\
                       "Following page %s is not a link" % str(linkNumber))
                linkNumber = linkNumber + 1
            pageCounter = int(pageCounter) + 1
            search_page_obj.click(search_page_obj.next_page_link, True, testsetup.timeout)
          
    def tearDown(self):
        self.selenium.stop()
