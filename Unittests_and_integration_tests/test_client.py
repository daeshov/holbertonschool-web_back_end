#!/usr/bin/env python3
"""
Unittests for client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ unittest for GithubOrgClient
    """
    @parameterized.expand([
        ('google', {}),
        ('abc', {})
    ])
    def test_org(self, test, result):
        """Test GithubOrgClient.org method
        """
        with patch("client.get_json") as gc:
            gc.return_value = {}
            gitclient = client
            gitclient = gitclient.GithubOrgClient(test)
            self.assertEqual(gitclient.org, result)
            gc.assert_called_once()


if __name__ == '__main__':
    unittest.main()
