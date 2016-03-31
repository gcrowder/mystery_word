import unittest
import mystery_word

class TestMysteryWord(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(mystery_word.open_file('test.txt'), ['house', 'mouse', 'louse', 'douse', 'souse'])

    def test_assert_not_equal(self):
        self.assertNotEqual(mystery_word.open_file(), ['house', 'mouse', 'louse', 'douse', 'souse'])




if __name__ == '__main__':
    unittest.main()
