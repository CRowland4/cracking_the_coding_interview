#  Implement a basic string compression method using the counts of repeated characters. For example, the string
#   aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string,
#   return the original string. String will have only uppercase and lowercase letters.
from io import StringIO


def string_compression(string: str) -> str:
    if len(string) <= 2:
        return string

    result = ""
    left, right = 0, 1

    count = 1
    while right < len(string):
        if string[left] == string[right]:
            count += 1
            left += 1
        else:
            result += f"{string[left]}" + str(count)
            count = 1
            left = right

        right += 1

    result += f"{string[left]}" + str(count)
    if len(result) < len(string):
        return result

    return string


# Optimal solution - just uses a more efficient way to concatenate strings
def string_compression_optimal(string: str) -> str:
    if len(string) <= 2:
        return string

    left, right = 0, 1
    count = 1

    string_builder = StringIO()
    while right < len(string):
        if string[left] == string[right]:
            count += 1
        else:
            string_builder.write(string[left])
            string_builder.write(str(count))
            count = 1
            left = right

        right += 1

    string_builder.write(string[left])
    string_builder.write(str(count))

    result = string_builder.getvalue()
    if len(result) >= len(string):
        return string

    return result
