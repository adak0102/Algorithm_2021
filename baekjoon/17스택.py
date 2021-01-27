#10773
import sys
N=int(sys.stdin.readline())

li=[]  #코드 짧은거 보고 기억 하기!!
for a in range(N):
    #더 빠른 한 줄 방법 있나?
    new=int(sys.stdin.readline())
    if new>=1:
        li.append(new)
    else:
        li.pop()
    #li.append( new if new >=1 else  )

#print(li)
print(sum(li))

##short
from sys import stdin
input()
l=[]
for i in map(int,stdin): #stdin으로 묶어서 한번에 받음 #map(int)
    l.append(i) if i else l.pop()  #한줄로 구현 # if i i 가 True면
print(sum(l))

#
import sys

N = int(input())

stack = []

K = list(map(int,sys.stdin.read().split()))

for i in K:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))
