import argparse
from rich.console import Console
import random

console = Console()

def find_words(sentence: str) -> None:
    """Finds and replaces words in the input sentence with random words of the same starting letter and length.
    
    :param sentence: The input sentence to generate words from. """

    words = sentence.lower().split()
    new_words = []
    for word in words:
        first_letter = word[0]
        length = len(word)
        word_list = []
        with open('words_alpha.txt', 'r') as file:
            for line in file:
                if line.startswith(first_letter) and len(line.strip()) == length:
                    word_list.append(line.strip())
        if word_list == []:
            new_word = word
        else:
            new_word = word_list[random.randint(0, len(word_list)-1)]
        new_words.append(new_word)

        new_sentence = ' '.join(new_words)
    return new_sentence

def main():
    """Main function to parse command line arguments and call find_words function."""
    
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence", help="Sentence to generate words from.")
    args = parser.parse_args()

    console.print(find_words(args.sentence))

if __name__ == '__main__':
    main()

