#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By

class QuestionsPage(Base):
    """
    'Ask a Question' landing page.
    """
    _page_title = 'Firefox Support Forum | Firefox Help'
    _forums_page_url = '/en-US/questions'
    _ask_question_link_locator = '/en-US/questions/new'
    _sort_solved_link_locator = (By.CSS_SELECTOR, 'a[href*="filter=solved"]')
    _sort_unsolved_link_locator = (By.CSS_SELECTOR, 'a[href*="filter=unsolved"]')
    _sort_no_replies_link_locator = (By.CSS_SELECTOR, 'a[href*="filter=no-replies"]')
    _questions_list_block_locator = (By.CSS_SELECTOR, 'ol.questions')
    _questions_list_locator = (By.CSS_SELECTOR, 'ol.questions > li')
    _question_list_link_locator = (By.CSS_SELECTOR, 'h2 > a')
    _solved_or_unsolved_text_locator = (By.CSS_SELECTOR, 'div.thread-meta > span')
    
    def go_to_forum_questions_page(self):
        self.open(self._forums_page_url)
        self.is_the_current_page

    def click_ask_new_questions_link(self):
        self.selenium.find_element(*self._ask_question_link_locator).click()
        return AskNewQuestionsPage(self.testsetup)

    def go_to_thread(self, url):
        self.open(url)

    def click_any_question(self, question_number):
        return self.selenium.find_elements(*self._questions_list_locator)[question_number - 1].find_element(*self._question_list_link_locator).click()

    def click_sort_by_solved_questions(self):
        self.selenium.find_element(*self._sort_solved_link_locator).click()

    def click_sort_by_unsolved_questions(self):
        self.selenium.find_element(*self._sort_unsolved_link_locator).click()

    def click_sort_by_no_replies_questions(self):
        self.selenium.find_element(*self._sort_no_replies_link_locator).click()

    @property
    def are_questions_present(self):
        return self.is_element_present(*self._questions_list_block_locator)

    @property
    def questions_count(self):
        return len(self.selenium.find_elements(*self._questions_list_locator))

    def sorted_list_filter_text(self, question_number):
        return self.selenium.find_elements(*self._questions_list_locator)[question_number - 1].find_element(*self._solved_or_unsolved_text_locator).text


class AskNewQuestionsPage(Base):
    """
    'Ask a New Question' page.
    Child class of Questions Page
    """
    _page_title = 'Ask a Question | Firefox Help'
    _questions_new_url = '/en-US/questions/new'
    _firefox_product_first_link_locator = (By.CSS_SELECTOR, 'ul.select-one > li > a')
    _category_prob_first_link_locator = (By.CSS_SELECTOR, 'ul.select-one > li > a')
    _type_question_box_locator = (By.NAME, 'search')
    _ask_this_button_locator = (By.CSS_SELECTOR, 'input[value="Ask this"]')
    _none_of_these_button_locator = (By.CSS_SELECTOR, 'input[value *="None"]')
    _provide_details_button_locator = (By.ID, 'show-form-btn')
    _q_content_box_locator = (By.ID, 'id_content')
    _q_site_box_locator = (By.ID, 'id_sites_affected')
    _q_trouble_box_locator = (By.ID, 'id_troubleshooting')
    _q_post_button_locator = (By.CSS_SELECTOR, 'input[value="Post Question"]')
    _sort_solved_link_locator = (By.CSS_SELECTOR, 'a[href*=filter=solved]')
    _sort_unsolved_link_locator = (By.CSS_SELECTOR, 'a[href*=filter=unsolved]')
    _sort_no_replies_link_locator = (By.CSS_SELECTOR, 'a[href*=filter=no-replies]')
    _questions_list_locator = (By.CSS_SELECTOR, 'ol.questions > li')
    _solved_or_unsolved_text_locator = (By.CSS_SELECTOR, 'div.thread-meta > span')

    def go_to_ask_new_questions_page(self):
        self.open(self._questions_new_url)
        self.is_the_current_page

    def click_firefox_product_link(self):
        self.selenium.find_element(*self._firefox_product_first_link_locator).click()

    def click_category_problem_link(self):
        self.selenium.find_element(*self._category_prob_first_link_locator).click()

    def type_question(self, question_to_ask):
        self.selenium.find_element(*self._type_question_box_locator).send_keys(question_to_ask)
        self.selenium.find_element(*self._ask_this_button_locator).click()

    def click_provide_details_button(self):
        self.selenium.find_element(*self._provide_details_button_locator).click()

    def fill_up_questions_form(self, q_text='details', q_site='www.example.com', q_trouble='no addons'):
        self.selenium.find_element(*self._q_content_box_locator).send_keys(q_text)
        self.selenium.find_element(*self._q_site_box_locator).send_keys(q_site)
        self.selenium.find_element(*self._q_trouble_box_locator).send_keys(q_trouble)
        self.selenium.find_element(*self._q_post_button_locator).click()

    @property
    def sorted_list_filter_text(self, question_number):
        return self.selenium.find_elements(*self._questions_list_locator)[question_number - 1].find_element(*self._solved_or_unsolved_text_locator).text


class ViewQuestionPage(Base):

    _question_locator = (By.CSS_SELECTOR, 'div.content > h1')
    _detail_locator = (By.CSS_SELECTOR, 'div.content > p')
    _problem_too_button_locator = (By.CSS_SELECTOR, 'input[value*="problem"]')
    _problem_count_text_locator = (By.CSS_SELECTOR, 'div[class^="have-problem"] > mark')
    _no_thanks_link_locator = (By.LINK_TEXT, 'No Thanks')

    @property
    def question(self):
        return self.selenium.find_element(*self._question_locator).text

    @property
    def question_detail(self):
        return self.selenium.find_element(*self._detail_locator).text

    def click_problem_too_button(self):
        self.selenium.find_element(*self._problem_too_button_locator).click()
        self.wait_for_element_present(*self._no_thanks_link_locator)

    @property
    def problem_count(self):
        count_text = self.selenium.find_element(*self._problem_count_text_locator).text
        count_text = count_text.split()
        return int(count_text[0])
