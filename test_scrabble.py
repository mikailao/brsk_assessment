import unittest
from scrabble import find_words

class ScrabbleTest(unittest.TestCase):
    def test_find_words(self) -> None:
        """Test that the find_words function returns a string with the same number of words, the same beginning letter and length for each word as the input sentence."""
        
        sentence = "this is a test sentence"
        output = find_words(sentence)

        for i in range(len(sentence.split())):
            word = sentence.split()[i]
            new_word = output.split()[i]
            self.assertEqual(len(word), len(new_word))
            self.assertEqual(word[0], new_word[0])
            self.assertEqual(len(sentence.split()), len(output.split()))

if __name__ == '__main__':
    unittest.main()