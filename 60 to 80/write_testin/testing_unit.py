import unittest
from full_name import full_name


class MyMainTest(unittest.TestCase):
    def test_first_last_name(self):
        correct_name = full_name('naeim', 'nobahari')
        self.assertEqual(correct_name, 'Naeim Nobahari')


if __name__ == '__main__':
    unittest.main()
