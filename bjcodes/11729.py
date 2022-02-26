
def hanoi(n,a,b,c):
  if(n == 1):
    print(a,c)
    return
  else:
    # n-1 를 A->B 로
    hanoi(n-1,a,c,b)
    # 1개를 A->C 로
    print(a, c)
    # n-1개를 B->C 로
    hanoi(n-1,b,a,c)


n = int(input())
print(pow(2,n)-1)
hanoi(n,1,2,3)
    
