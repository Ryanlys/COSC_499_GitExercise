import unittest, sort_string_desc


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sort_string_desc.sort_string(['a','b','c','d']), ['d','c','b','a']) #sorted array should be in descending order


if __name__ == '__main__':
    unittest.main()
