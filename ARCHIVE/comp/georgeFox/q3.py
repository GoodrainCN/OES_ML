num = int(input())
nums = []
for i in range(num):
    nums.append(input())
total = 0
for num in nums:
    num = str(num)
    if num[0] != "T":
        total += float(num)
    else:
        total += float(num[2::]) * (1 + 0.0825)
print('The total is $' + str(format(total, ".2f")))