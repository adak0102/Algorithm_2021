#18258
# from collections import deque
# def push(x):
#     global deq
#     deq.append(x)
# def pop():
#     global deq
#     if deq:
#         print(deq.popleft())
#     else:
#         print(-1)
# def size():
#     global deq
#     print(len(deq))
# def empty():
#     global deq
#     if deq:
#         print(0)
#     else:
#         print(1)
# def front():
#     global deq
#     if deq:
#         print(deq[0])
#     else:
#         print(-1)
#
# def back():
#     global deq
#     if deq:
#         print(deq[-1])
#     else:
#         print(-1)
#
#
# deq=deque([])
# import sys
# N=int(sys.stdin.readline().rstrip())
# for a in range(N):
#     list=sys.stdin.readline().rstrip().split()
# #    print(list)
#     input=list[0]
#     #print(input)
#     if input=='push':
#         push(list[1])
#     elif input=='pop':
#         pop()
#     elif input=='size':
#         size()
#     elif input == 'empty':
#         empty()
#     elif input == 'front':
#         front()
#     elif input == 'back':
#         back()

# import sys
# from collections import deque
#
#
# def push(queue, x):
#     queue.append(x)
#
#
# def pop(deque):
#     return deque.popleft() if deque else -1
#
#
# def size(queue):
#     return len(queue)
#
#
# def empty(queue):
#     return 1 if not queue else 0
#
#
# def front(queue):
#     return queue[0] if queue else -1
#
#
# def back(queue):
#     return queue[-1] if queue else -1
#
#
# deque = deque()
#
# N = int(sys.stdin.readline().rstrip())
#
# for _ in range(N):
#     order = sys.stdin.readline().rstrip().split()
#
#     command = order[0]
#
#     if (command == "push"):
#         push(deque, order[1])
#     elif (command == "pop"):
#         sys.stdout.write(str(pop(deque)) + "\n")
#     elif (command == "size"):
#         sys.stdout.write(str(size(deque)) + "\n")
#     elif (command == "empty"):
#         sys.stdout.write(str(empty(deque)) + "\n")
#     elif (command == "front"):
#         sys.stdout.write(str(front(deque)) + "\n")
#     elif (command == "back"):
#         sys.stdout.write(str(back(deque)) + "\n")

# deque안쓰고 풀기
# from sys import stdin
# input()
# s, com= [], stdin.readlines()
# cnt = 0
# for x in com:
#     c = x.split()
#     if c[0] == "push":
#         s.append(c[1])
#     elif c[0] == 'pop':
#         if len(s) > cnt:
#             print(s[cnt])
#             cnt += 1
#         else: print(-1)
#     elif c[0] == 'size':
#         print(len(s)-cnt)
#     elif c[0] == 'empty':
#         if len(s) == cnt :
#             print(1)
#             cnt = 0
#             s = []
#         else: print(0)
#     elif c[0] == 'front':
#         if len(s) > cnt: print(s[cnt])
#         else: print(-1)
#     elif c[0] == 'back':
#         if len(s) > cnt: print(s[-1])
#         else: print(-1)
#  가장 앞을 가르키는 인덱스 값을 가지고 있는 것입니다. 위의 소스코드의 cnt가 해당 역할을 합니다.
# pop기능을 수행하면 가장 앞 인덱스 cnt에 해당되는 부분을 출력하고 cnt에 1을 더해서 가장 앞쪽을 가르키는 인덱스를 그 다음 칸을 가르키도록 합니다.
# 초기화를 위해서 queue를 구현한 리스트가 비어있을 경우 전체 데이터를 초기화해주었습니다

#11866 OOOO ***
# import sys
# from collections import deque
#
# N,step=map(int,sys.stdin.readline().rstrip().split())
#
# list=deque([ _ for _ in range(1,N+1) ])
# new=[]
# i=1
# while list:
#     #for i in range(N):
#     if i % step == 0 :
#         new.append(list.popleft())
#     else:
#         list.append(list.popleft())
#     i+=1
#     #if i==N:
#      #   i=0
#
#         #else:
#
#             #list.leftpop(i)
#
# new=deque(map(str,new))
# #print(new)
# print('<',', '.join(new),'>',sep='')

#1966
from collections import deque
import sys

N=int(sys.stdin.readline().rstrip())
n,index=map(int, sys.stdin.readline().rstrip().spli())
# for a in range(N):
cnt=0
while i<=len(A):
