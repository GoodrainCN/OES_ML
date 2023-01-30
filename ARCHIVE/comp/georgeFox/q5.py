data = []
for i in range(10):
    line = input()
    line = line.split(" ")
    data = data + line

num = int(input())
nums = []
for i in range(num):
    nums.append(input())

def get_index(word0):
    count = 0
    index_list = []
    # for i in range(len(word0)):
    #     index_list.append(i)
    for letter in word0:
        if letter != "*":
            index_list.append(count)
        count += 1
    return index_list


def check(word0, word1):
    if len(word0) != len(word1):
        return False
    index0 = get_index(word0)
    letter_list0 = []
    letter_list1 = []
    for index in index0:
        letter_list0.append(word0[index])
        letter_list1.append(word1[index])
    if letter_list0 == letter_list1:
        return True
    else:
        return False

result = []

for word in nums:
    temp = []
    for item in data:
        if check(word, item) == True:
            temp.append(item)
    result.append(temp)
# print(result)

for i in result:
    if len(i) == 0:
        print("NO MATCH")
        continue
    for j in i:
        print(j,end=" ")
    print()