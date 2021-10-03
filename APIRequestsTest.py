from APIRequests import get_repo
from APIRequests import get_commit
from APIRequests import display_repo

import unittest

class TestDisplay(unittest.TestCase):
    def testGetRepo1(self):
        self.assertEqual(get_repo('Keyodinfire')[0], 'Complexity')

    def testGetRepo2(self):
        self.assertEqual(get_repo("Keyodinfire")[4], 'GitHubAPI567')

    def testGetCommit1(self):
        self.assertEqual(get_commit('Keyodinfire', 'Triangle567'), 5)

    def testGetCommit2(self):
        self.assertEqual(get_commit('Keyodinfire', 'CS545Project'), 10)

    def testDisplayRepo1(self):
        self.assertEqual(display_repo()[1], 'Repo: CS545Project Number of Commits: 10')

    def testDisplayRepo2(self):
        self.assertEqual(display_repo()[9], 'Repo: SSW345-HW5 Number of Commits: 2')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()