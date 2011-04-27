# -*- coding: utf-8 -*-
from selenium import selenium
import vars
import unittest
import sumo_functions


class search_unknownchars(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(
        vars.ConnectionParameters.server,
        vars.ConnectionParameters.port,
        vars.ConnectionParameters.browser,
        vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def test_search_unknownchars(self):
        sel = self.selenium
        sumo_func = sumo_functions.SUMOfunctions()
        # We're checking to ensure that
        # "unknown" characters like
        #  "�" don't appear
        sumo_func.open(sel,
        "/search?where=all&locale=ja&q=%E3%83%96%E3%83%83%E3%82%AF%E3%83%9E" +
        "%E3%83%BC%E3%82%AF%E3%81%AE%E6%95%B4%E7%90%86&sa")
        self.failUnless(sel.is_text_present(u"ブックマークの整理"))
        self.failIf(sel.is_text_present(u"�"))

    def tearDown(self):
        self.selenium.stop()

if __name__ == "__main__":
    unittest.main()
