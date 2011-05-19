import pytest

import search_page

@pytest.mark.smoketests
class TestCantFindWhatYouAreLookingFor:

    def test_cant_find_what_youre_looking_for_test(self,testsetup):
        search_page_obj       = search_page.SearchPage(testsetup)
        
        searchTerms = ["firefox", "bgkhdsaghb"]
        for current_search_term in searchTerms:
            search_page_obj.go_to_search_page()
            search_page_obj.do_search_on_search_box(current_search_term)

            assert search_page_obj.is_text_present(\
                "Can't find what you're looking for?"),\
                "Can't find text not present"
            assert search_page_obj.is_element_present(\
                "link=Ask a support question instead!"),\
                "Ask question link not present"

