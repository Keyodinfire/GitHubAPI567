from APIRequests import get_repo
from APIRequests import get_commit
from APIRequests import display_repo

import unittest
import json
from unittest.mock import patch

class TestDisplay(unittest.TestCase):

    @patch('requests.get', response = 'Complexity')
    def testGetRepo1(self, mock):
        self.assertEqual(get_repo('Keyodinfire'), 'Complexity')

    @patch('APIRequests.get_repo', return_value='GitHubAPI567')
    def testGetRepo2(self, mock):
        self.assertEqual(get_repo("Keyodinfire")[4], 'GitHubAPI567')

    @patch('APIRequests.get_commit', return_value=5)
    def testGetCommit1(self, mock):
        self.assertEqual(get_commit('Keyodinfire', 'Triangle567'), 5)

    @patch('APIRequests.display_repo', return_value=10)
    def testGetCommit2(self, mock):
        self.assertEqual(get_commit('Keyodinfire', 'CS545Project'), 10)

    @patch('APIRequests.display_repo', return_value='Repo: CS545Project Number of Commits: 10')
    def testDisplayRepo1(self, mock):
        self.assertEqual(display_repo()[1], 'Repo: CS545Project Number of Commits: 10')

    @patch('APIRequests.display_repo', return_value='Repo: Node.js_Application_Lab Number of Commits: 4')
    def testDisplayRepo2(self, mock):
        self.assertEqual(display_repo()[9], 'Repo: Node.js_Application_Lab Number of Commits: 4')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()