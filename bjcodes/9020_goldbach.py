#  골드바흐의 추측.

#  소수 판별 함수
def isPrime(x):
  if x == 1:
    return False
  for i in range(2,x):
    if x % i == 0:
      return False
  return True

n = int(input())
array = []
for _ in range(n):
  array.append(int(input()))
temp = 0

for x in array:
  temp = int(x/2)
  if isPrime(temp):
    print(temp,temp)
    continue
  a,b = temp-1, temp+1
  while a > 1:
    if isPrime(a) and isPrime(b):
      break
    else: 
      # 2 로 했다가 오답. temp-1 temp+1이 짝수인 경우...ex a = 18  
      a -= 1
      b += 1
  print(a,b)
