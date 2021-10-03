import unittest

from HW_4a import request

class TestGithub(unittest.TestCase):

    def testUserNotFound(self): 
        self.assertEqual(request('dsjkgnjnregklnel3252'),'Unable to find user with the inputted ID.')

    def testValidResponse(self): 
        self.assertEqual(len(request('jlora23')),10)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
