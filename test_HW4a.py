import unittest
from unittest import mock
from HW_4a import request

class TestGithub(unittest.TestCase):

    @mock.patch("HW_4a.request")
    def testUserNotFound(self, mock_get):
        mock_get.return_value = "Unable to find user with the inputted ID."
        self.assertEqual(mock_get.return_value, "Unable to find user with the inputted ID.")

    @mock.patch("HW_4a.request")
    def testValidResponse(self, mock_get):
        mock_get.return_value = 11
        self.assertEqual(mock_get.return_value,11)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
