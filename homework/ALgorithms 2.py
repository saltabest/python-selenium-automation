# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_2(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
         add = 1
    left = s[: half + add]
    right = s[half + add:]
    return right == left

test_string_odd =  "aaabccc"
test_string_even = "aaabbb"
print(split_2(test_string_odd))
print(split_2(test_string_even))


# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def unique_characters(s):
    lenstr = len(s)
    lenset = len(set(s))
    return lenset == lenstr

test_data_positive = "abcde"
test_data_negative = "abccd"
print(unique_characters(test_data_positive))
print(unique_characters(test_data_negative))
