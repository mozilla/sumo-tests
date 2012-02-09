#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from sumo_page import SumoPage


class QuestionsPage(SumoPage):
    """
    'Ask a Question' landing page.
    """
    _page_title = 'Firefox Support Forum'
    _forums_page_url = '/en-US/questions'
    _ask_question_link_locator = '/en-US/questions/new'
    _question_list_link_locator = "css=ol.questions > li:nth-child(%d) > div:nth-child(1) > h2 > a"
    _sort_solved_link_locator = "css=a[href*='filter=solved']"
    _sort_unsolved_link_locator = "css=a[href*='filter=unsolved']"
    _sort_no_replies_link_locator = "css=a[href*='filter=no-replies']"
    _solved_or_unsolved_text_locator = "css=ol.questions > li:nth-child(%s) > div.thread-meta > span"
    _questions_list_block_locator = "css=ol.questions"
    _questions_list_xpath_locator = "//ol[@class='questions']/li"

    def go_to_forum_questions_page(self):
        self.open(self._forums_page_url)
        self.is_the_current_page

    def click_ask_new_questions_link(self):
        self.click(self._ask_question_link_locator, True, self.timeout)
        return AskNewQuestionsPage(self.testsetup)

    def go_to_thread(self, url):
        self.selenium.open(url)

    def click_any_question(self, num):
        q_link = self._question_list_link_locator % num
        self.selenium.click(q_link)
        self.selenium.wait_for_page_to_load(self.timeout)

    def click_sort_by_solved_questions(self):
        self.selenium.click(self._sort_solved_link_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def click_sort_by_unsolved_questions(self):
        self.selenium.click(self._sort_unsolved_link_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def click_sort_by_no_replies_questions(self):
        self.selenium.click(self._sort_no_replies_link_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    def are_questions_present(self):
        try:
            return self.selenium.is_element_present(self._questions_list_block_locator)
        except:
            return False

    @property
    def get_questions_count(self):
        return int(self.selenium.get_xpath_count(self._questions_list_xpath_locator))

    def get_sorted_list_filter_text(self, question_number):
        locator = self._solved_or_unsolved_text_locator % question_number
        return self.selenium.get_text(locator)


class AskNewQuestionsPage(SumoPage):
    """
    'Ask a New Question' page.
    Child class of Questions Page
    """
    _page_title = 'Ask a Question'
    _questions_new_url = '/en-US/questions/new'
    _firefox_product_first_link_locator = 'css=ul.select-one > li > a'
    _category_prob_first_link_locator = 'css=ul.select-one > li > a'
    _type_question_box_locator = 'search'
    _ask_this_button_locator = "css=input[value='Ask this']"
    _none_of_these_button_locator = "css=input[value *='None']"
    _provide_details_button_locator = "show-form-btn"
    _q_content_box_locator = 'id_content'
    _q_site_box_locator = 'id_sites_affected'
    _q_trouble_box_locator = 'id_troubleshooting'
    _q_post_button_locator = "css=input[value='Post Question']"
    _sort_solved_link_locator = "css=a[href*=filter=solved]"
    _sort_unsolved_link_locator = "css=a[href*=filter=unsolved]"
    _sort_no_replies_link_locator = "css=a[href*=filter=no-replies]"
    _solved_or_unsolved_text_locator = "css=ol.questions > li:nth-child(%s) > div.thread-meta > span"
    _questions_list_block_locator = "css=ol.questions"
    _questions_list_xpath_locator = "//ol[@class='questions']/li"

    def go_to_ask_new_questions_page(self):
        self.selenium.open(self._questions_new_url)
        self.is_the_current_page

    def click_firefox_product_link(self):
        self.click(self._firefox_product_first_link_locator, True, self.timeout)

    def click_category_problem_link(self):
        self.click(self._category_prob_first_link_locator, True, self.timeout)

    def type_question(self, question_to_ask):
        self.type(self._type_question_box_locator, question_to_ask)
        self.click(self._ask_this_button_locator, True, self.timeout)

    def click_provide_details_button(self):
        self.click(self._provide_details_button_locator, True, self.timeout)

    def fill_up_questions_form(self, q_text='details', q_site='www.example.com', q_trouble='no addons'):
        self.type(self._q_content_box_locator, q_text)
        self.type(self._q_site_box_locator, q_site)
        self.type(self._q_trouble_box_locator, q_trouble)
        self.click(self._q_post_button_locator, True, self.timeout)

    def get_sorted_list_filter_text(self, question_number):
        locator = self._solved_or_unsolved_text_locator % question_number
        return self.selenium.get_text(locator)


class ViewQuestionPage(SumoPage):

    _question_locator = "css=div.content > h1"
    _detail_locator = "css=div.content > p"
    _problem_too_button_locator = "css=input[value*='problem']"
    _problem_count_text_locator = "css=div[class^='have-problem'] > mark"
    _no_thanks_link_locator = "link=*No*Thanks*"

    @property
    def question(self):
        return self.selenium.get_text(self._question_locator)

    @property
    def question_detail(self):
        return self.selenium.get_text(self._detail_locator)

    def click_problem_too_button(self):
        self.selenium.click(self._problem_too_button_locator)
        self.wait_for_element_present(self._no_thanks_link_locator)

    @property
    def problem_count(self):
        count_text = self.selenium.get_text(self._problem_count_text_locator)
        count_text = count_text.split()
        return int(count_text[0])
