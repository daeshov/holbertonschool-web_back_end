#!/usr/bin/env python3
"""utils test module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, requests, memoize


class TestAccessNestedMap(unittest.TestCase):
    """unittest for nested map
    """
    # test case
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


class TestGetJson(unittest.TestCase):
    """test for Getjson
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """test to return mock json object
        """
        mock_object = Mock()
        mock_object.json.return_value = payload
        with patch('requests.get', return_value=mock_object):
            this_json = get_json(url)
        mock_object.json.assert_called_once()
        self.assertEqual(this_json, payload)


if __name__ == '__main__':
    unittest.main()
