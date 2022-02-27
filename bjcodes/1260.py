from collections import deque

n, m, v = map(int,input().split())

#graph 구성하기
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for g in graph:
  g.sort()

#dfs
def dfs(graph,v,visited):
  visited[v] = True
  print(v,end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

#bfs 
def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v,end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(graph,v,visited)
visited = [False]*(n+1)
print()
bfs(graph,v,visited)
