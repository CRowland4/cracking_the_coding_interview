# Assume you have a method is_substring which checks if one word is a substring of another. Given two strings, write a
#   function to check if the second string is a rotation of the first string using only one call to is_substring.
# For example, "waterbottle" is a rotation of "erbottlewat"


def is_rotation(string1: str, string2: str) -> bool:
    if string1 and string2 and (len(string1) == len(string2)):
        return string2 in (string1 + string1)


print(is_rotation("erbottlewat", "waterbottle"))
