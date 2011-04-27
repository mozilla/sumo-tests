'''
Created on Aug 12, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import other_support_page

class TestOtherSupport(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)


    def tearDown(self):
        self.selenium.stop()

    def test_other_support_page(self):
        sel                    = self.selenium
        other_support_page_obj = other_support_page.OtherSupportPage(sel)
        
        other_support_page_obj.go_to_other_support_page()
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.moz_community_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.moz_zine_forum_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.faq_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.win_bbs_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.netscape_faq_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.silly_dog_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.tbird_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.moz_news_link))
        self.failUnless(other_support_page_obj.is_text_present(other_support_page_obj.alt_fan_text))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.irc_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.chatzilla_link))
        self.failUnless(other_support_page_obj.is_element_present(other_support_page_obj.fx_channel_link))

if __name__ == "__main__":
    unittest.main()