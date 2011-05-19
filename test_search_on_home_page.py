'''
Created on Jun 25, 2010

@author: mozilla
'''
import pytest

import support_home_page
import search_page

@pytest.mark.smoketests
class TestSearchOnHomePage:

    def test_search_on_home_page(self,testsetup):
        support_home_page_obj = support_home_page.SupportHomePage(testsetup)
        search_page_obj       = search_page.SearchPage(testsetup)
                 
        search_term = 'iphone'
        support_home_page_obj.go_to_support_home_page()
        support_home_page_obj.do_search_on_main_search_box(search_term,search_page_obj)

        url = search_page_obj.get_url_current_page()
        assert search_term in url, "Search term %s does not exist in the url %s" %(search_term,url)