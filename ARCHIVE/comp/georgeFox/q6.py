datas = []

datacount = int(input())
for i in range(datacount):
 howmany = int(input())
 data = input()
 data = [float(value) for value in data.split()]
 datas.append(data)

for data in datas:
 ran = max(data[1::]) - min(data[1::])
 accvalue = data[0]
 ave = sum(data[1::]) / len(data[1::])
 acc = abs(accvalue - ave)

 if ((-1)* 0.05) <= acc <= 0.05:
  if ran <= 0.1*ave:
   print('Both')
  else:
   print('Accurate')
 elif ran <= 0.10*ave:
  print('Precise')
 else:
  print('Neither')