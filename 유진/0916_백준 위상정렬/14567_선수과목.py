v,e = map(int, input().split())

result = [1]*(v+1)
edge=[]

for _ in range(e):
  a,b = map(int, input().split())
  edge.append((a,b))

edge.sort(key=lambda x: (x[1], x[0]))

for i in edge:
  result[i[1]]= max(result[i[1]], result[i[0]]+1)

print(*result[1:])