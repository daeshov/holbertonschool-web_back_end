#!/usr/bin/env python3
"""
Unittests for client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
import client
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos, TEST_PAYLOAD


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

    @patch("client.get_json", return_value={'key': '12345'})
    def test_public_repos(self, get_json_mock):
        """
        """
        get_json_mock()
        with patch(
            'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as msk:
            msk.return_value = {'key': '12345'}
            test_obj = client
            test_obj = test_obj.GithubOrgClient('another_test')
            next = test_obj._public_repos_url
            self.assertEqual(
                next, msk.return_value
            )
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, dict_license, key_license, expc_result):
        """
        """
        github_client = client.GithubOrgClient('test_org')
    
        self.assertEqual(
            github_client.has_license(dict_license, key_license),
            expc_result
        )

@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos", "license_key"),
        TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """GithubOrgClient.public_repos method in an integration test.
    That means that we will only mock code that sends external requests.
    """    
    @classmethod
    def setUpClass(cls):
        """set-up class
        """        
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

if __name__ == '__main__':
    unittest.main()
