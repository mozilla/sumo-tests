'''
Created on Aug 12, 2010

@author: mozilla
'''
import pytest

import other_support_page

@pytest.mark.fft
class TestOtherSupport:

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
