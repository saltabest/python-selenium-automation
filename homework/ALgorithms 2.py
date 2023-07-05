
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

def unique_characters(s):
    lenstr = len(s)
    lenset = len(set(s))
    return lenset == lenstr

test_data_positive = "abcde"
test_data_negative = "abccd"
print(unique_characters(test_data_positive))
print(unique_characters(test_data_negative))
