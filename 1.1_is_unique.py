# Given a string, determine if a string has all unique characters.
def is_unique(string: str) -> bool:
    return len(set(string)) == len(string)


# Considerations: empty string, a sentence with spaces but unique letters will fail because the space is repeated
print(is_unique("this isn't unique"))  # False
print(is_unique("but I'm"))  # True
print(is_unique("I am not"))  # False - because of the spaces


# What if you can't use additional data structures?
def is_unique2(string: str) -> bool:
    for i, char_i in enumerate(string):
        for char_j in string[i + 1:]:
            if char_i == char_j:
                return False

    return True


print(is_unique("this isn't unique"))  # False
print(is_unique("but I'm"))  # True
print(is_unique("I am not"))  # False - because of the spaces


# Official solution - though this technically violates the "additional data structures" constraint
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


print(is_unique_optimal("this isn't unique"))  # False
print(is_unique_optimal("but I'm"))  # True
print(is_unique_optimal("I am not"))  # False - because of the spaces
