#!/usr/bin/env python3
"""utils test module
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """unittest for nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, map):
        """test for nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), map)

    @parameterized.expand([
       ({}, ("a,")),
       ({"a": 1}, ("a", "b"))
    ])

    def test_access_nested_map_exception(self, nested_map, path):
      """to test that a KeyError is raised for
      the following inputs
      """
      with self.assertRaises(KeyError):
          access_nested_map(nested_map, path)

    

if __name__ == '__main__':
    unittest.main()
