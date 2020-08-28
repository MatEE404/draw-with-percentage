# -*- coding: utf-8 -*-

import unittest
from draw_with_percentage import draw_with_percentage


class TestRandomness(unittest.TestCase):

    def test_draw_with_percentage_without_errors(self):
        raised = False
        for _ in range(0, 10000):
            obj = [
                ["milk", "23.401"],
                ["apple", "25.91"],
                ["bread", "39.09"],
                ["banana", "11.599"]
            ]

            try:
                draw_with_percentage(obj)
            except:
                raised = True
                break

        self.assertFalse(raised, 'Exception raised')

    def test_draw_with_percentage_with_bad_inputs(self):
        with self.assertRaises(ValueError):
            draw_with_percentage([])
        with self.assertRaises(ValueError):
            draw_with_percentage([
                ["milk1", 50],
                ["milk2", 50]
            ])
        with self.assertRaises(ValueError):
            draw_with_percentage([
                [1, 50],
                [2, 50]
            ])
        with self.assertRaises(ValueError):
            draw_with_percentage([
                ["1", "50"],
                ["2", "49.9"]
            ])
