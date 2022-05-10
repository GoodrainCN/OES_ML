data = []
for i in range(4):
    line = input()
    line = line.split()
    data = data + line
    
new_data = []
for i in data:
    new_data.append(i.lower())
    
num = int(input())
nums = []
for i in range(num):
    nums.append(input())

def get_index(word0):
    word0 = str(word0)
    index_list = []
    count = 0
    for letter in word0:
        if letter not in new_data:
            index_list.append(count)
        count += 1
    return index_list


def check_word(word0):
    result = "yes"
    index_list = get_index(word0)
    word0 = str(word0)
    for i in index_list:
        if i != 0 and i != len(word0) - 1:
            if word0[i-1:i+1] in new_data or word0[i:i+2] in new_data:
                pass
            else:
                result = "no"
                return result
        elif i == 0:
            if word0[i:i+2] in new_data:
                pass
            else:
                result = "no"
                return result
        elif i == len(word0) - 1:
            if word0[i-1:i+1] in new_data:
                pass
            else:
                result = "no"
                return result
    return result

for num in nums:
    print(check_word(num))