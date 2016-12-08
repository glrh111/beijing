#! /usr/bin/env python
#! coding: utf-8

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/glrh11/Documents/google/chromedriver')

    def test_can_start_a_list_and_receive_it_later(self):
        self.browser.get('http://localhost:8000/')
        assert 'To-Do' in self.browser.title

    def tearDown(self):
        self.browser.quit()



if __name__ == '__main__':
    unittest.main()