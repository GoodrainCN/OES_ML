def dist(num):
    
    num_l = 0
    num_m = 0
    num_s = 0
    
    if num >= 4:
        num_l = int(num/4)
        res_p = num % 4
        if res_p >= 2:
            num_m = int(res_p/2)
            res_p_ = res_p % 2
            if res_p_ >= 1:
                num_s = int(res_p_ / 1)
        else:
            num_s = int(res_p / 1)
    elif num >= 2:
        num_m = int(num/2)
        res_p = num % 2
        if res_p >= 1:
            num_s = int(res_p / 1)
    else:
        num_s = int(num/1)
    
    str_l = ""
    str_m = ""
    str_s = ""
    
    # if num_l > 0 and num_m > 0:
    #     str_l  = str(num_l) + " large "
    # if num_l > 0 and num_s > 0:
    #         str_l  = str(num_l) + " large "   
    # if num_l > 0:
    #     str_l  = str(num_l) + " large"
    # if num_m > 0 and num_l > 0:
    #     str_m = str(num_m) + " medium "
    # if num_m > 0 and num_s > 0:
    #     str_m = str(num_m) + " medium "
    # if num_m > 0:
    #     str_m = str(num_m) + " medium "
    # if num_s > 0:
    #     str_s = str(num_s) + " small"
    
    # print(num_l, num_m, num_s)
    
    if num_l > 0:
        str0 = str(num_l) + " large"
        if num_m > 0:
            str0 = str0 + " " + str(num_m) + " medium"
            if num_s > 0:
                str0 = str0 + " " + str(num_s) + " small"
        elif num_s > 0:
            str0 = str0 + " " + str(num_s) + " small"
    elif num_m > 0:
        str0 = str(num_m) + " medium"
        if num_s > 0:
            str0 = str0 + " " + str(num_s) + " small"
    elif num_s > 0:
        str0 = str(num_s) + " small"
    
    # str0 = str_l + str_m + str_s
    
    return str0

num = int(input())
nums = []
for i in range(num):
    nums.append(int(input()))
for num in nums:
    str0 = dist(num)
    print(str0)