#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
Created on March 27, 2012

@author: mozilla
'''
from pages.page import Page

class PageProvider(Page):
    ''' internal methods '''
    def _go_to_page(self, page_object, do_login=False, user='default'):
        self.selenium.get(self.base_url_ssl + page_object._page_url)
        page_object.is_the_current_page
        if (do_login):
            page_object.sign_in(user)
        return page_object

    ''' pages for which login is optional '''
    def provide_home_page(self, do_login=False, user='default'):
        from pages.desktop.support_home_page import SupportHomePage
        return self._go_to_page(SupportHomePage(self.testsetup), do_login, user)
    
    ''' pages for which login is required '''
    def provide_kb_new_article(self, user='admin'):
        home_page = self.provide_home_page(True, user)
        from pages.desktop.knowledge_base_new_article import KnowledgeBaseNewArticle
        return self._go_to_page(KnowledgeBaseNewArticle(self.testsetup))
        
