import sys


# 시간초과 문제 -> sys 
q = []
result2 = []
def push(x) :
  q.append(x)
def pop():
  if not q:
    result2.append('-1')
  else:
    result = q.pop()
    result2.append(result)
  
def top():
  if not q:
    result2.append('-1')
  else:
    result2.append(str(q[-1]))

def empty():
  if not q:
    result2.append('1')
  else:
    result2.append('0')
  
def size():
  result2.append(str(len(q)))

n = int(sys.stdin.readline())
for i in range(n):
  command = sys.stdin.readline().rstrip()
  
  if ''.join(command[0:3]) == 'pus':
    func, x = map(str,command.split(' '))
    push(x)
  elif ''.join(command[0:3]) == 'pop':
    pop()
  elif ''.join(command[0:3]) == 'top':
    top()
  elif ''.join(command[0:3]) == 'siz':
    size()
  elif ''.join(command[0:3]) == 'emp':
    empty()
  else:
    print("defualt")

for r in result2:
  sys.stdout.write(r+'\n')
