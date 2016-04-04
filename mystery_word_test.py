import unittest
import mystery_word

test_words = ['i', 'spoke', 'to', 'several', 'people', 'with', 'delayed', 'sleep', 'phase', 'a', 'condition', 'that', 'congressional']



class TestMysteryWord(unittest.TestCase):

    def test_assert_equal_get_words(self):
        self.assertEqual(mystery_word.get_words('test.txt'), ['house', 'mouse', 'louse', 'douse', 'souse'])

    def test_assert_not_equal(self):
        self.assertNotEqual(mystery_word.get_words(), ['house', 'mouse', 'louse', 'douse', 'souse'])

    def test_assert_equal_difficulty_1(self):
        self.assertEqual(mystery_word.make_appropriate_difficulty(test_words, 'EASY'), ['spoke', 'people', 'with', 'sleep', 'phase', 'that'])

    def test_assert_equal_difficulty_2(self):
        self.assertEqual(mystery_word.make_appropriate_difficulty(test_words, 'NORMAL'), ['several', 'people', 'delayed'])

    def test_assert_equal_difficulty_3(self):
        self.assertEqual(mystery_word.make_appropriate_difficulty(test_words, 'HARD'), ['condition', 'congressional'])

    def test_assert_not_equal_difficulty_1(self):
        self.assertNotEqual(mystery_word.make_appropriate_difficulty(test_words, 'EASY'), ['several', 'people', 'delayed'])

    def test_assert_not_equal_difficulty_2(self):
        self.assertNotEqual(mystery_word.make_appropriate_difficulty(test_words, 'NORMAL'), ['spoke', 'people', 'with', 'sleep', 'phase', 'that'])

    def test_assert_not_equal_difficulty_3(self):
        self.assertNotEqual(mystery_word.make_appropriate_difficulty(test_words, 'HARD'), ['spoke', 'people', 'with', 'sleep', 'phase', 'that'])

    def test_assert_equal_show_word(self):
        self.assertEqual(mystery_word.show_word('general', ['e', 'f', 'j', 'a', 'l', 'g']), ['g', 'e', '_', 'e', '_', 'a', 'l'])

    def test_assert_true_is_guessed(self):
        self.assertTrue(mystery_word.is_guessed('spoke', ['r', 'o', 'k', 't', 's', 'e', 'p']))


if __name__ == '__main__':
    unittest.main()
