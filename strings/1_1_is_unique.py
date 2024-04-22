# Given a string, determine if a string has all unique characters.
def is_unique(string: str) -> bool:
    return len(set(string)) == len(string)


# What if you can't use additional data structures?
def is_unique2(string: str) -> bool:
    for i, char_i in enumerate(string):
        for char_j in string[i + 1:]:
            if char_i == char_j:
                return False

    return True


# Considerations:
#   - What is the allowed character set?


# Official solution, using other data structures
def is_unique_optimal(string: str) -> bool:
    # Assumes that the string exclusively contains ASCII characters
    if len(string) > 128:
        return False

    values = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if values[val]:
            return False

        values[val] = True

    return True


# Another potential solution, though the sorted method produces a list, which is an additional data structure
def is_unique_optimal2(string: str) -> bool:
    string = "".join(sorted(string))
    for i, char in enumerate(string[:len(string) - 1]):
        if char == string[i + 1]:
            return False

    return True


print(is_unique_optimal2("this isn't unique"))  # False
print(is_unique_optimal2("but I'm"))  # True
print(is_unique_optimal2("I am not"))  # False - because of the spaces
