
data = list(input().split('-'))
result = 0

for i in range(len(data)):
  # ** list x map x
  data1 = data[i].split("+")
  
  a = 0
  for d in data1:
    a += int(d)
  if i == 0:
    result += a
  else:
    result -= a

print(result)
