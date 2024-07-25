import argparse
from rich.console import Console
import random

console = Console()

def find_words(sentence):
    words = sentence.split()
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
            new_word = word_list[random.randint(0, len(word_list))]
        new_words.append(new_word)

        new_sentence = ' '.join(new_words)
    console.print(new_sentence)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence", help="Sentence to generate words from.")
    args = parser.parse_args()

    find_words(args.sentence)

if __name__ == '__main__':
    main()

