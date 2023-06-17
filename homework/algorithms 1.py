def sumn (n):
    result = 0
    for x in range(n+1):
        result = result + x
    return result
test_data = 5
test_result = sumn(test_data)
print(test_result)

def find_max (a,b,c):
    if a >b and a>c:
        return a
    if b > a and b> c:
        return b
    return c

test_result = find_max (5,10,20)
print (test_result)

def count_odd (n):
    odd = 0
    even = 0
    while n != 0:
        current_digit = n%10
        if current_digit %2:
            odd += 1
        else:
            even += 1
            n = n/10
    print("evens: {evens}, odd: {odd}")
test_num = 1457
count_odd(test_num)

