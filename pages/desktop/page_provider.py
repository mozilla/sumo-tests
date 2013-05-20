#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page

from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

class PageProvider():
    ''' internal methods '''

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium

    def _set_window_small(self, width, height, zoom_level):
        self.selenium.set_window_size(width, height)
        el_window = self.selenium.switch_to_active_element()
        if zoom_level < 100:
            el_window.send_keys(Keys.CONTROL,Keys.SUBTRACT) #100->90%
        if zoom_level < 90:
            el_window.send_keys(Keys.CONTROL,Keys.SUBTRACT) #90->80%
        if zoom_level < 80:
            el_window.send_keys(Keys.CONTROL,Keys.SUBTRACT) #80->67%    
        
    def _set_zoom_default(self):    
        el_window = self.selenium.switch_to_active_element()
        el_window.send_keys(Keys.CONTROL,'0') #100%     
        
    def _go_to_page(self, page_object, do_login=False, user='default'):
        #self.selenium.maximize_window()
        dim = self.selenium.get_window_size()
        self._set_window_small(0.9*dim['width'], 0.9*dim['height'], 67)
        self.selenium.get(self.base_url + page_object._page_url)
        page_object.is_the_current_page
        if (do_login):
            page_object.sign_in(user)
        return page_object

    def _go_to_page_with_login_redirect(self, page_object, user='default'):
        #self.selenium.maximize_window()
        self.selenium.set_window_size(700,500)
        
        from pages.desktop.login_page import LoginPage
        self.selenium.get(self.base_url + page_object._page_url)
        login_page = LoginPage(self.testsetup)
        login_page.log_in(user)
        page_object.is_the_current_page
        return page_object

    ''' pages for which login is forbidden '''

    def new_user_registration_page(self):
        from pages.desktop.register_page import RegisterPage
        return self._go_to_page(RegisterPage(self.testsetup))

    ''' pages for which login is optional '''

    def home_page(self, do_login=False, user='default'):
        from pages.desktop.support_home_page import SupportHomePage
        return self._go_to_page(SupportHomePage(self.testsetup), do_login, user)

    def new_question_page(self, do_login=True, user='default'):
        from pages.desktop.questions_page import AskNewQuestionsPagec
        return self._go_to_page(AskNewQuestionsPage(self.testsetup), do_login, user)

    def questions_page(self, do_login=False, user='default'):
        from pages.desktop.questions_page import QuestionsPage
        return self._go_to_page(QuestionsPage(self.testsetup), do_login, user)

    def search_page(self, do_login=False, user='default'):
        from pages.desktop.search_page import SearchPage
        return self._go_to_page(SearchPage(self.testsetup), do_login, user)

    def refine_search_page(self, do_login=True, user='default'):
        from pages.desktop.refine_search_page import RefineSearchPage
        return self._go_to_page(RefineSearchPage(self.testsetup), do_login, user)

    ''' pages for which login is required '''

    def new_kb_article_page(self, user='admin'):
        from pages.desktop.knowledge_base_new_article import KnowledgeBaseNewArticle
        return self._go_to_page_with_login_redirect(KnowledgeBaseNewArticle(self.testsetup), user)
