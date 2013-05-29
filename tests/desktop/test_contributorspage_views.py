#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

#from pages.page import Page
from pages.desktop.page_provider import PageProvider
from selenium.webdriver.common.by import By
from pages.desktop.utils import Utils

from pages.desktop.contributors_page import ContributorsPage
from selenium import webdriver
from unittestzero import Assert

@pytest.mark.skipif("config.getvalue('base_url')=='https://support-dev.allizom.org'")
class TestContributorsPageViews():
            
    #locators
    _loc_contributors_header = (By.XPATH, ".//*[@id='for-contributors']/header/h1")
    _loc_contributors_links = (By.XPATH, ".//*[@id='for-contributors']/section/ul/li")
    _loc_target_link = (By.CSS_SELECTOR, "a")
        
    @pytest.mark.nondestructive
    def test_page_first_level_views_from_home(self, mozwebqa):      
        
        #go to the home page
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        
        utils = Utils(mozwebqa)
        
        #[H] click the link to open the menu "for contributors"
        menu_link = utils.find_element_and_wait(self._loc_contributors_header)
        if menu_link is not None:
            menu_link.click()    #open the menu
        else:
            print "test_page_first_level_views_from_home: failed to find the menu.\n"
            return
        
        #[H] find links in the menu
        links = utils.find_elements_and_wait(self._loc_contributors_links)
        num_links = len(links)

        #[H] click and back each one of the links
        for i in range(num_links):
            
            #select a target link
            target_link = links[i]
            
            #[H] go to a click-able link and click it
            link = utils.find_element_and_wait(self._loc_target_link,target_link)
            if link is None:
                print "a link within for the contributors menu was not found.\n"
                break 
            else:
                link_addr = link.get_attribute("href")
                link.click()
                
            #[M] validate the reached URL
            if utils.match_urls(link_addr) == False:
                print "destination of the link does not match the href attribute.\n"
            #   break
            
            #[H] back to the home page
            utils.go_back_page()
        
            #[H] click the link to open the menu "for contributors" again
            utils.find_element_and_wait(self._loc_contributors_header).click()
            
            #[H] find links in the menu again
            links = utils.find_elements_and_wait(self._loc_contributors_links)
        
        return
    
    @pytest.mark.nondestructive
    def test_quickstart_guide(self, mozwebqa):
        
        _loc_quickstart_guide = (By.XPATH, ".//*[@id='for-contributors']/section/ul//li/a[text()='Quickstart Guide']")
        _loc_involvements = (By.XPATH, "//div[@class='grid_3']")
        _loc_inv_link = (By.CSS_SELECTOR, "a")
        
        #go to the home page
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        
        #open an instance of Utils
        utils = Utils(mozwebqa)
        
        #[H] click the link to open the menu "for contributors"
        menu_link = utils.find_element_and_wait(self._loc_contributors_header)
        if menu_link is not None:
            menu_link.click()    #open the menu
        else:
            print "test_quickstart_guide: failed to find the menu.\n"
            return  
        
        #[H] click the link to the quickstart guide
        guide_link = utils.find_element_and_wait(_loc_quickstart_guide)
        if guide_link is not None:
            guide_link.click()    #open the menu
        else:
            print "test_quickstart_guide: failed to find the target link.\n"
            return 
        
        #[M] find involvement elements (links)
        involvement_links = utils.find_elements_and_wait(_loc_involvements)
        if involvement_links is None:
            print "test_quickstart_guide: failed to find links to involvements.\n"
            return
        else:
            num_involvements = len(involvement_links)
            for i in range(num_involvements):
                involvement_link = involvement_links[i]
                #[H] click a link to one of the involvements                
                utils.find_element_and_wait(_loc_inv_link,involvement_link).click()
                #[H] back to the home page
                utils.go_back_page()        
                #[M] find involvement elements (links) again
                involvement_links = utils.find_elements_and_wait(_loc_involvements)
                
    @pytest.mark.nondestructive
    def test_news_and_resources(self, mozwebqa): 
        
        _loc_news_and_resources = (By.XPATH, ".//*[@id='for-contributors']/section/ul//li/a[text()='News & Resources']")
        _loc_toc = (By.XPATH, "//div[@id='toc']/ul//a")
        _loc_articles = (By.XPATH, "//article//section//ul//li/a")
        
        #go to the home page
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')
        
        #open an instance of Utils
        utils = Utils(mozwebqa)
        
        #[H] click the link to open the menu "for contributors"
        menu_link = utils.find_element_and_wait(self._loc_contributors_header)
        if menu_link is not None:
            menu_link.click()    #open the menu
        else:
            print "test_news_and_resources: failed to find the menu.\n"
            return  
        
        #[H] click the link to the news & resources
        guide_link = utils.find_element_and_wait(_loc_news_and_resources)
        if guide_link is not None:
            guide_link.click()    #open the menu
        else:
            print "test_news_and_resources: failed to find the target link.\n"
            return
        
        #[M] find TOC elements (links)
        TOC_links = utils.find_elements_and_wait(_loc_toc)
        if TOC_links is None:
            print "test_news_and_resources: failed to find links to involvements.\n"
            return
        else:
            #num_TOCs = len(TOC_links)
            num_TOCs = 1
            for i in range(num_TOCs):
                TOC_link = TOC_links[i]
                #[H] click a link to one of the TOCs  
                TOC_link.click()
                #[H] find all the associated articles             
                article_links = utils.find_elements_and_wait(_loc_articles)
                num_article_links = len(article_links)
                for j in range(num_article_links):
                    article_link = article_links[j]
                    if article_link is not None:
                        article_link.click()    #open the menu
                    else:
                        print "test_news_and_resources: failed to find links to articles.\n"
                        return      
                    #[H] back to the home page
                    utils.go_back_page()
                        