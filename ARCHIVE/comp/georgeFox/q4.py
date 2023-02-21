answer = []
sentences = []
infos = []
articles = input()
articles = articles.split()
help1 = input()
help1 = help1.split()
help2 = input()
help2 = help2.split()
datacount = int(input())
for i in range(datacount):
 info = input()
 info = info.split()
 infos.append(info)
 for i in range(int(info[1])):
  sentence = input()
  sentences.append(sentence.lower())
for i in range(len(infos)):
 for sentence in sentences:
  sentence = sentence.split()
  temp = []
  temp.append(sentence[-1][0:len(sentence[-1])-1])
  sentence.remove(sentence[-1])
  temp = ''.join(temp)
  sentence.append(temp)
  if infos[i][0] in sentence:
   if sentence[sentence.index(infos[i][0])-1] in articles:
    answer.append('NOUN')
   elif sentence[sentence.index(infos[i][0])-1] in help1 or sentence[sentence.index(infos[i][0])-1] in help2:
    answer.append('VERB')
 answer.append('')
for i in answer[0:-1]:
 print(i)