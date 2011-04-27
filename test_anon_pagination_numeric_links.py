from selenium import selenium
import vars
import unittest
import time
import support_home_page
import search_page

class anon_pagination_numeric_links(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_anon_pagination_numeric_links(self):
        sel = self.selenium
        
        support_hp_obj  = support_home_page.SupportHomePage(sel)
        search_page_obj = search_page.SearchPage(sel)

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
            if(not(sel.is_text_present(search_word))):
                sel.refresh()
                sel.wait_for_page_to_load(vars.ConnectionParameters.page_load_timeout)
                time.sleep(2)
                counter = counter+1
            else:
                not_found = False
        pageCounter = 1
        # store the last link
        url = "/search?q=%s" %(search_word)
        search_page_obj.open(url)
        if(sel.is_element_present("css=ol.pagination > li:nth-child(7)")):
            lastLink = int(sel.get_text("css=ol.pagination > li:nth-child(7)"))
        else:
            return
        # Iterate over every page of hits...
        while (sel.is_element_present(search_page_obj.next_page_link)
               and int(pageCounter) + 1 <= int(lastLink) - 3):
            # Verify that all page numbers previous to current page ARE active
            linkNumber = 1
            while int(linkNumber) < int(pageCounter):
                if int(linkNumber) < int(pageCounter) - 3:
                    linkNumber = linkNumber + 1
                    continue
                self.failUnless(
                    sel.is_element_present("link=" + str(linkNumber)),
                    "Previous page %s is not a link" % str(linkNumber))
                linkNumber = linkNumber + 1
            # Verify that all page numbers following current page ARE active
            linkNumber = int(pageCounter) + 1
            while int(linkNumber) <= int(pageCounter) + 3:
                self.failUnless(
                    sel.is_element_present("link=" + str(linkNumber)),
                    "Following page %s is not a link" % str(linkNumber))
                linkNumber = linkNumber + 1
            pageCounter = int(pageCounter) + 1
            search_page_obj.click(search_page_obj.next_page_link, True, vars.ConnectionParameters.page_load_timeout)
          
    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
