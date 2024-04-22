#  Given a string, write a function to check if it is a permutation of a palindrome (not limited to dictionary words)
import unittest
from collections import Counter


# Palindromes come in two types - those with an even number of characters, and those with an odd number.
#   Those with an even number of characters will have an even number of each unique character, because each "half" of
#       the palindrome will contain exactly half of the letters.
#   Palindromes with an odd number of characters will have one character that appears an odd number of times (this will
#       be the middle character), and the rest of the characters will appear an even number of times.
def pp(string: str) -> bool:
    odds = 0
    string = string.replace(" ", "").lower()
    for char in set(string):
        if string.count(char.lower()) % 2 == 1:
            odds += 1
            if odds > 1:
                return False

    return True


# Book solution, using the same idea as above, just implemented a bit differently
def pp_optimal(string: str) -> bool:
    string = string.replace(" ", "").lower()
    counter = Counter()
    for char in string:
        counter[char] += 1

    odds = 0
    for key in counter:
        if counter[key] % 2 == 1:
            odds += 1
            if odds > 1:
                return False

    return True


# Alternate book solution, without using counts - assumes all letters
def pp_optimal2(string: str) -> bool:
    string = string.replace(" ", "").lower()
    odd = [0 for _ in range(26)]
    for i, char in enumerate(string):
        location = ord(char) - ord("a")
        odd[location] = (odd[location] + 1) % 2

    return sum(odd) <= 1


class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pp(self):
        for [test_string, expected] in self.data:
            actual = pp_optimal2(test_string)
            self.assertEqual(actual, expected)

    def test_pp_optimal(self):
        for [test_string, expected] in self.data:
            actual = pp_optimal(test_string)
            self.assertEqual(actual, expected)

    def test_pp_optimal2(self):
        for [test_string, expected] in self.data:
            actual = pp(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
