def judge(t_list):
    t_list = t_list
    result = True
    if len(t_list) == 1:
        return True
    for i in range(len(t_list)-1):
        #print(t_list[i], t_list[i+1])
        if t_list[i] != t_list[i+1]:
            result = False
            break
    return result

def get_index(t_list):
    t_list = t_list
    temp = 0
    mini = t_list[0] + t_list[1]
    start = 0
    end = 1
    for i in range(len(t_list)-1):
        temp = t_list[i] + t_list[i+1]
        #print(temp)
        if temp <= mini:
            mini = temp
            start = i
            end = i+1
    return start,end
        
def modi(index0, index1, t_list):
    # index0 = get_index[0]
    # index1 = get_index[1]
    var0 = t_list.pop(index0)
    var1 = t_list.pop(index1-1)
    # print(t_list)
    new_var = var0 + var1
    t_list.insert(index0, new_var)
    return t_list

def get_count(list0: list) -> int:
    count = 0
    for i in range(len(list0)-1):
        if judge(list0) == True:
            return count
        index0 = get_index(list0)[0]
        index1 = get_index(list0)[1]
        list0 = modi(index0, index1, list0)
        count += 1
    return count

numOfCases = int(input())
for i in range(numOfCases):
    lenOfIn = int(input())
    stringOfIn = input()
    listOfIn = stringOfIn.split(" ")
    listOfIn = [int(i) for i in listOfIn]
    print(listOfIn)
    # print(get_count(listOfIn))
