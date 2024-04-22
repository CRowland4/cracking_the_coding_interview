#  There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a
#   character. Given two strings, write a function to check if they are one edit (or zero edits) away from each other.


def one_away(str1: str, str2: str) -> bool:
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) == len(str2):  # Same length, so this checks replacement
        differences = 0
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                differences += 1
                if differences > 1:
                    return False
        return True

    if len(str1) > len(str2):
        longer = str1
        shorter = str2
    else:
        longer = str2
        shorter = str1

    l, s = 0, 0
    while l < len(longer) and s < len(shorter):
        if shorter[s] != longer[l]:
            if l != s:
                return False
            l += 1
        else:
            s += 1
            l += 1

    return True




