# Scrabble Sentence Generator

## Table of Contents

- [Assignment](#assignment)
- [Solution Overview](#solution-overview)
- [Requirements](#requirements)
- [Execution](#execution)
- [Example](#example)
- [Testing](#testing)

## Assignment 

Write a program that takes a sentence as an input and returns a new sentence with words that have the same number of letters and begin with the same letter as each word in the input sentence. The program should return different words each time the program is run with the same input sentence. 

## Solution Overview

The program iterates through the input sentence and finds words that have the same length and first letter for each word. It then generates an array with all the words that fit the criteria, and selects a word at random to replace the original word in the sentence. 

## Requirements

The program was written in Python 3.12.4. It uses the following libraries:
 - random
 - argeparse
 - rich
 - unittest

```random```, ```argeparse``` and ```unittest``` are included in the Python standard library. To install ```rich```, run the following command in your terminal:

```pip install rich```

## Execution

To run the program, execute the following command in your terminal with the input sentence as an argument:

```python scrabble.py "input sentence"```

The program will return the new sentence. 

## Example

```python scrabble.py "The quick brown fox jumps over the lazy dog"```

## Testing 

To run the test, execute the following command in your terminal:

```python test_scrabble.py```

The program will indicate whether the test has passed or failed.
