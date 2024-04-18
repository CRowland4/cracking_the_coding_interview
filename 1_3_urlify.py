import unittest
#  Write a method to replace all spaces in a string with '%20'.


def urlify(string: str) -> str:
    return string.replace(" ", "%20")


#  Optimal solution - problem states that string will already have space for the extra characters, and that it's safe to
#     assume that the "true" length of the string (without spaces at the end) is also give. The string will be a list of
#     characters in this case.
def urlify_optimal(string: list, length: int) -> list:
    current_index = len(string)

    for i in reversed(range(length)):
        if string[i] == " ":
            string[current_index - 3:current_index] = "%20"
            current_index -= 3
        else:
            string[current_index - 1] = string[i]
            current_index -= 1

    return string


class Test(unittest.TestCase):
    cases = [
        ("this is a test", "this%20is%20a%20test"),
        ("   ", "%20%20%20"),
    ]

    def test_urlify(self):
        for case in Test.cases:
            assert urlify(case[0]) == case[1]


class TestOptimal(unittest.TestCase):
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify_optimal(self):
        for [test_string, length, expected] in self.data:
            actual = urlify_optimal(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
