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

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url property
        """
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
                ) as gc:
            gc.return_value = {'repos_url': 'test.io'}
            org_client = client
            org_client = org_client.GithubOrgClient('test_org')
            self.assertEqual(
                org_client.org['repos_url'], org_client._public_repos_url
            )

if __name__ == '__main__':
    unittest.main()
