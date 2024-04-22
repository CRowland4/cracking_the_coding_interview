# Given two strings, write a method to decide if one is a permutation of the other
import unittest
from collections import defaultdict


def is_permutation(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


def is_permutation2(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    for char in str1:
        str2 = str2.replace(char, "", 1)

    return not bool(str2)


# Considerations:
#   - Should it be case-sensitive?
#   - Is whitespace significant?
#   - Also doesn't hurt to ask about character set on this one too.


# Optimal solution
def is_permutation_optimal(str1: str, str2: str) -> bool:
    counter = defaultdict(int)
    for char in str1:
        counter[char] += 1
    for char in str2:
        if counter[char] == 0:
            return False
        counter[char] -= 1

    return True


class Test(unittest.TestCase):
    trues = [("cat", "tac"), ("123456789a;sldkfj", "a;fjsldk192837465")]
    falses = [("foo", "bar"), ("racecar", " racecar")]

    def test_is_permutation(self):
        for pair in Test.trues:
            self.assertTrue(is_permutation(pair[0], pair[1]))
        for pair in Test.falses:
            self.assertFalse(is_permutation(pair[0], pair[1]))

        return

    def test_is_permutation2(self):
        for pair in Test.trues:
            self.assertTrue(is_permutation2(pair[0], pair[1]))
        for pair in Test.falses:
            self.assertFalse(is_permutation2(pair[0], pair[1]))

        return

    def test_is_permutation_optimal(self):
        for pair in Test.trues:
            self.assertTrue(is_permutation_optimal(pair[0], pair[1]))
        for pair in Test.falses:
            self.assertFalse(is_permutation_optimal(pair[0], pair[1]))

        return


if __name__ == "__main__":
    unittest.main()
