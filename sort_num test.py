import unittest, sort_num


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sort_num.sort_num([3,2,1]), [1,2,3]) #sorted array should be ascending


if __name__ == '__main__':
    unittest.main()
