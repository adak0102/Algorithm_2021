#1260
# from collections import defaultdict
# from collections import deque
#
# #재귀
# def dfs(node):
#     #방문할때만 dfs를 도는 거니까 node를 프린트 해줌
#     print(node,end=' ')
#     #S가 갈 수 있는 경우의 수를 먼저 감
#     #시작점이 갈 수 있는 노드 루프 돔
#     for i in V[node]:
#         #방문한 적이 없으면 dfs 실시 , 있으면 넘어감
#         if visited[i]==0:
#             #방문했다고 먼저 표시해주고
#             visited[i]=1
#             #재귀돌아야함
#             dfs(i)
#
# #데큐
# #dfs 실행 시에 0,1로 방문처리 되어있기 때문에, 여기선 True,False로 방문 처리
# def bfs(S):
# #### 정형화 bfs 코드################
#     #첨에 큐를 만들 것
#     q=deque()
#     #첨에 시작점을 노드로 놓는다
#     q.appendleft(S) # 데큐 모습 : -> ['''''[S]]
#     visited[S]=1
# #### 정형화 bfs 코드################
#     #q가 없어질때까지 while문을 돈다
#     while q:
#         #q는 처음 시작한 node니까 pop으로 뽑아옴, q가 빌 때까지
#         node=q.pop()
#         #프린트는 넣을때 해도 되고 뺄떄 해도 됨
#         print(node,end=' ')
#         #i는 nextnode가 됨
#         for i in V[node] :
#             if visited[i]==0:
#                 # 방문되지 않으면 i를 큐에 넣음
#                 q.appendleft(i)
#                 #이제 방문 됨
#                 visited[i]=1
#     # 다 없어질때까지 pop을 돈다
#
#
####base####
# N,M,S=map(int,input().split())
# V=defaultdict(list)
#
# #딕트로 푼당~~~!!!
# for _ in range(M):
#     a,b = map(int, input().split())
#     V[a].append(b)
#     V[b].append(a)
#
# #작은것부터 먼저도니까, 정렬시켜줌
# for key in V:
#     V[key].sort()
#
# #방문한 노드 알기 위한
# #노드 개수만큼 설정하고 , 방문하면 1로 , 1234 인덱스로 쓰기 위해 N+1로 놓음
# visited=[0]*(N+1)
# #첫방문은 1로
# visited[S]=1
# dfs(S)
#
# print()
# visited=[0]*(N+1)
# bfs(S)

#2606
# import sys
# from collections import deque
# from collections import defaultdict
# N=int(sys.stdin.readline().rstrip())
# M=int(sys.stdin.readline().rstrip())
#
# V=defaultdict(list)
# visited=[0]*(N+1)
#
# for i in range(M):
#     n,m=map(int,sys.stdin.readline().rstrip().split())
#     V[n].append(m)
#     V[m].append(n)
#
# def bfs():
#     q=deque()
#     visited[1]=1
#     q.appendleft(1)
#     cnt=0
#     while q :
#         node=q.pop()
#
#         for a in V[node]:
#             if visited[a]==0:
#                 q.appendleft(a)
#                 visited[a]=1
# bfs()
# cnt=-1
# for a in visited:
#     if a==1:
#         cnt+=1
# print(cnt)







#2667 혼자 실패
# import sys
# from collections import deque
# # from collections import defaultdict
# N=int(sys.stdin.readline().rstrip())
#
# array=[]
# for line in range(N):
#     arr=list(sys.stdin.readline().rstrip())
#     array.append(arr)
# #print(array)
# visited=[ [0 for _ in range(N)] for _ in range(N)]
#
# deq=deque()
# for a in range(N):
#     for b in range(N):
#         if visited[a][b]==0:
#             visited[a][b]=1
#         if array[a][b]==1:
#             #deq.appendleft([a,b])
#             for

## 2667 ㅇㅈ
# from collections import deque
# from collections import defaultdict
#
# def bfs(i,j):
#     q=deque()
#     q.appendleft((i,j))
#     apart[i][j]='-1'
#     dir=[(1,0),(-1,0),(0,1),(0,-1)]
#     ans=1
#
#     while q:
#         x,y =q.pop()
#         #방향설정
#         for d in dir:
#             nx,ny=x+d[0],y+d[1]
#             if 0<= nx < N and 0 <= ny < N: #이거 아님 밖으로 나오는 거니까
#                 if apart[nx][ny] =='1': #방문 안한 새로운 아파트
#                     q.append((nx,ny)) #q에 어펜드 해줌
#                     apart[nx][ny]='-1' #방문했단 표시로 -1로 바꿔줌
#                     ans+=1
#     return ans
#
# N=int(input())
# #아파트 방문이력
# apart=[]
#
# #1
# for _ in range(N):
#     apart.append(list(input()))
#

# cnt=0
# result=[]
#
# # 2. n by n 탐색
# for i in range(N):
#     for j in range(N):
#         if apart[i][j]=='1': #1이면 아파트인데 #1이면 bfs 탐색
#             cnt+=1
#             result.append(bfs(i,j))
# print(cnt)
# print(*sorted(result),sep='\n')

##2667(다시)
# from collections import deque
#
# def bfs(i,j):
#     q=deque()
#     q.appendleft((i,j))
#     ans=1
#     apart[i][j]='-1'
#     dir=[[-1,0],[0,-1],[1,0],[0,1]]
#     ans=1
#
#
#     while q:
#         x,y=q.pop()
#         for d in dir:
#             xn,yn=x+d[0],y+d[1]
#             if 0<=xn<=N and 0<=yn<=N:
#                 if apart[xn][yn]=='1':
#                     ans+=1
#                     q.append((xn,yn))
#                     apart[xn][yn]='-1'
#                     ans+=1
#     return ans
#
#
#
# N=int(input())
# cnt=0
# apart=[]
# result=[]
#
# for _ in range(N):
#     apart.append(list(input()))
#
# for a in range(N):
#     for b in range(N):
#         if apart[a][b]=='1':
#             cnt+=1
#             result.append(bfs(a,b))
# print(cnt)
# print(*sorted(result))
#

# ## dfs
# from collections import defaultdict
#
# N,M,S=int(input().split())
# V=defaultdict(list)
#
# for a in range(N):
#     a,b=map(int,input().split())
#     V[a].append(b)
#     V[b].append(a)
#
# Visited=[0]*(N+1)
# Visited[S]=1
#
# for key in V:
#     V[key].sort()
#
# def dfs(node):
#     print(node)
#     for i in V[node]:
#         if not i in Visited: #if Visited[i]==0:
#             Visited[i]=1
#             dfs(i)
#
#     # need_visit=deque()
#     # if need_visit
#
# ## bfs
# from collections import deque
# from collections import defaultdict
#
# N,M,S=map(int, input().split())
# V=defaultdict(list)
# for a in range(N):
#     a,b=map(int, input().split())
#     V[a].append(b)
#     V[b].append(a)
#
# Visited=[0]*(N+1)
#
# def bfs(node):
#     need_visit=deque()
#     need_visit.appendleft(node)
#     Visited[node]=1
#     # for i in V[node]:
#     #     if i not in Visited:
#     #         need_visit.appendleft(i)
#     #         need_visit.pop()
#     #         Visited[i]=1
#
#     while need_visit:
#         node=need_visit.pop()
#         print(node)
#         for i in V[node]:
#             if i not in Visited:
#                 need_visit.appendleft(i)
#                 Visited[i]=1

#1012
# test=int(input())
# M,N,L=map(int,input().split())
#
# for a in range(N):
#
#
# def bfs():
#


#
# #2178
# N,M=map(int,input().split())
# def bfs():
#


#7576
from collections import deque
from collections import defaultdict
a,b=map(int,input().split())

# for i in range(a):
ripe=[]
for j in range(b):
        ripe.append(list(input()))

for i in range(a):
    for j in range(b):
        if ripe[i][j]==1:
            q.append([i,j])
            #         if apart[a][b]=='1':
            #             cnt+=1
            #result.append(bfs(a,b))
            # print(cnt)
            # print(*sorted(result))



def bfs(i,j,):
    q=deque()
    q.appendleft((i,j))
    ans=1
    ripe[i][j]='-1'
    dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    ans=1

    while q :
        x, y = q.pop()
            for d in dir:
                xn,yn=x+d[0],y+d[1]
                if 0<=xn<=b and 0<=yn<=a:
                    if ripe[xn][yn]=='1':
                        q.append((xn,yn))
                        ripe[xn][yn]='-1'
                        #ans+=1
        return ans

#
# N=int(input())
# cnt=0
# apart=[]
# result=[]
#
# for _ in range(N):
#     apart.append(list(input()))
#
# for a in range(N):
#     for b in range(N):
#         if apart[a][b]=='1':
#             cnt+=1
#             result.append(bfs(a,b))
# print(cnt)
# print(*sorted(result))
#


import sys
from collections import deque

def bfs(riped,zero_cnt):
    result=0
    direction = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우
    while riped:
        x, y, day = riped.pop()

        if result < day : result=day

        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                if tomato_map[nx][ny] == 0:
                    tomato_map[nx][ny] = 1
                    zero_cnt-=1
                    riped.appendleft((nx,ny,day+1))
    return result if zero_cnt==0 else -1


M, N = map(int, sys.stdin.readline().split()) # 열, 행

tomato_map = []
riped = deque() # 익은 토마토의 위치가 저장되는 곳
zero_cnt=0
for i in range(N): # 행
    tomato_map.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M): # 열
        if tomato_map[i][j] == 1:
            riped.appendleft((i,j,0))
        elif tomato_map[i][j] == 0:
            zero_cnt+=1
print(bfs(riped,zero_cnt))


#1697
N,M=map(int,input().split())
def bfs():
    q=deque()
    q.append(N)
    while q: