def below_am(arr):
    am = sum(arr) / len(arr)
    for x in arr:
        if x < am:
            final_result.append(x)
    return final_result

test_list = [1,3,5,6,4,10,2,3]
test_result = below_am(test_list)
print(test_result)

def find_two_lowest(arr):
    arr.sort()
    return arr[:2]

test_list = [3,7,2,1,10,97,4]
result = find_two_lowest(test_list)
print(result)
