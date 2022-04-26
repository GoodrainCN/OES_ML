num = int(input())
data = []
for i in range(num):
    data.append(input())

cleaned = {}
index_list = []
status = []
for item in data:
    #index_list.append(item.split()[0])
    temp = item.split()
    cleaned[temp[0]] = temp[1::]
    
leng = len(cleaned)
    #print(item.split())#
#print(index_list)
#leng = set(index_list)
num_d = 0
num_l = 0
num_b = 0
num_n = 0
num_c = 0

for key in cleaned:
    if cleaned[key][0] == "DEAD":
        num_d += 1
        # print(cleaned[key])
        if cleaned[key][2] == 'NATURAL':
            num_n += 1
        elif cleaned[key][2] == 'MOUNTAIN':
            num_l += 1
        elif cleaned[key][2] == 'BEAR':
            num_b += 1
        elif cleaned[key][2] == 'COYOTE':
            num_c += 1
    
perc_sur = round(((leng - num_d) / leng)*100)
perc_lion = round((num_l / leng) * 100)
perc_bear = round((num_b / leng) * 100)
perc_coy = round((num_c / leng) * 100)
perc_nat = round((num_n / leng) * 100)

dict1 = {
    "MOUNTAIN LION": perc_lion,
    "NATURAL CAUSES": perc_nat,
    "COYOTE" : perc_coy,
    "BEAR" : perc_bear
}
sorted_values = dict1.values()# Sort the values
sorted_dict = {}

sorted_d = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

print("ALIVE"+" "+str(perc_sur)+"%")
for term in sorted_d:
    print(term[0]+" "+str(term[1])+"%")