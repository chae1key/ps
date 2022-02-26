# a - 97 ~ z - 122
# A 65~ Z 90

array = input()

count = [0]*(ord('Z')+1)

for i in range(0,len(array)):
  if(array[i]) >= 'a':
    count[ord(array[i])-32] += 1
  else:
    count[ord(array[i])] += 1
    
m = max(count)
result = []

for i in range(ord('A'),ord('Z')+1):
  if(m == count[i]):
    result.append(chr(i))

if(len(result) > 1):
  print("?")
else:
  print(result[0])
