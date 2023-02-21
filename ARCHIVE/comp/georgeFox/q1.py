# def is_alprime(num):
#     list0 = []
#     for i in range(1,num+1):
#         if num % i == 0:
#             list0.append(i)
#     if len(list0) == 3:
#         return True
#     else:
#         return False
    
# num_list = []
# for i in range(41):
#     if is_alprime(i) == True:
#         num_list.append(i)
        
data = [4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209, 2809, 3481, 3721, 4489, 5041, 5329, 6241, 6889, 7921, 9409, 10201, 10609, 11449, 11881, 12769, 16129, 17161, 18769, 19321, 22201, 22801, 24649, 26569, 27889, 29929, 32041]
num = int(input())
nums = []
for i in range(num):
    nums.append(int(input()))
for num in nums:
    print(data[num-1])