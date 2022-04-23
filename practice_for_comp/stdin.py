def is_prime(num):
    result = True
    if num < 2 or type(num) != int:
        result = False
        return result
    else:
        for i in range(2,num):
            if num % i == 0:
                result = False
                result
    return result

def ispalin(x):
    x = str(x)
    first = 0
    last = len(x)-1
    status = 1
    while first < last:
        if x[first] == x[last]:
            first+=1
            last-=1
        else:
            status = 0
            break
    return int(status)

num = int(input())
nums = []
for i in range(num):
    nums.append(int(input()))
for num in nums:
    if is_prime(num) == True and num >= 10 and ispalin(num) == 1:
        print("yes")
    else:
        print("no")