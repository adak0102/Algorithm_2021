#10828번
# import sys
#
# def push(x):
#     stack.append(x)
#
# def pop():
#     if len(stack)==0:
#         return -1
#     else:
#         return stack.pop()
# def size():
#     return len(stack)
#
# def empty():
#     if len(stack)==0:
#         return 1
#     else:
#         return 0
# def top():
#     if len(stack)==0:
#         return -1
#     else:
#         return stack[-1]
#
# #전역 변수부
# N=int(sys.stdin.readline().rstrip())
# stack=[]
#
# for a in range (N) :
#     new=sys.stdin.readline().rstrip().split()
#     if new[0]=='push':
#         push(new[1])
#     elif new[0]=='pop':
#         print(pop())
#     elif new[0]=='size':
#         print(size())
#     elif new[0]=='empty':
#         print(empty())
#     elif new[0]=='top':
#         print(top())

#S
# import sys
#
# # 정수 X를 스택에 넣는 연산이다.
# def push(x):
#     stack.append(x)
#
# # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
# # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# def pop():
#     if(not stack):  ### if (not stack) ********
#         return -1
#     else:
#         return stack.pop()
#
# # 스택에 들어있는 정수의 개수를 출력한다.
# def size():
#     return len(stack)
#
# # 스택이 비어있으면 1, 아니면 0을 출력한다.
# def empty():
#     return 0 if stack else 1  ## if stack****
#
# # 스택의 가장 위에 있는 정수를 출력한다.
# # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# def top():
#     return stack[-1] if stack else -1
#
# N = int(sys.stdin.readline().rstrip())
# stack = []
#
# for _ in range(N):
#     input_split = sys.stdin.readline().rstrip().split()
#
#     order = input_split[0]
#
#     if order == "push":   #"push" ""안줘서 디버깅!!!
#         push(input_split[1])
#     elif order == "pop":
#         print(pop())
#     elif order == "size":
#         print(size())
#     elif order == "empty":
#         print(empty())
#     elif order == "top":
#         print(top())

#toomuch
# list=[]
# for a in range(int(sys.stdin.readline().rstrip())):
#     run=sys.stdin.readline().rstrip().split()
#     #print(run)
#     if run[0]=='push':
#         list.append(run[1])
#         #print(list)
#     elif run[0]=='pop':
#         count = 0
#         for a in range(len(list)):
#             n = len(list) - 1 - a
#             if type(list[n]) == int:
#                 print(list[n])
#                 del(list[n])
#                 count += 1
#         if count==0:
#             print(-1)
#     elif run[0]=='top':
#         count=0
#         for a in range(len(list)):
#             n=len(list)-1-a
#             if type(list[n])==int:
#                 count+=1
#                 print(list[n])
#         if count==0:
#             print(-1)
#     elif run[0]=='size':
#         print(len(list))
#     elif run[0]=='empty':
#         if len(list)==0:
#             print(1)
#         else:
#             print(0)
#

#10773
# import sys
# N=int(sys.stdin.readline())
#
# li=[]  #코드 짧은거 보고 기억 하기!!
# for a in range(N):
#     #더 빠른 한 줄 방법 있나?
#     new=int(sys.stdin.readline())
#     if new>=1:
#         li.append(new)
#     else:
#         li.pop()
#     #li.append( new if new >=1 else  )
#
# #print(li)
# print(sum(li))
#
# ##short
# from sys import stdin
# input()
# l=[]
# for i in map(int,stdin): #stdin으로 묶어서 한번에 받음 #map(int)
#     l.append(i) if i else l.pop()  #한줄로 구현 # if i i 가 True면
# print(sum(l))

#
# import sys
#
# N = int(input())
#
# stack = []
#
# K = list(map(int,sys.stdin.read().split()))
#
# for i in K:
#     if i == 0:
#         stack.pop()
#     else:
#         stack.append(i)
#
# print(sum(stack))

#9012 번
import sys

# N=int(sys.stdin.readline().rstrip())
# for a in range(N):
#     #stack = []
#     sum=0
#     for b in list(sys.stdin.readline().rstrip()): #split()
#         #print(b)
#         if b=='(':
#         #    stack.append(1)
#             sum+=1
#         elif b==')':
#             #if len(stack)>=1:
#             #    stack.pop()
#             if sum>=1:
#                 sum-=1
#             else:
#                 sum='NO'
#             #    print('NO')
#     #print(stack)
#     # if len(stack)==0:
#     #     print('YES')
#     # else:
#     #     print('NO')
#     if sum==0:
#         sum='YES'
#     else:
#         sum='NO'
#     print(sum)



#왜 런타임 에러나?????????
# N=int(sys.stdin.readline().rstrip())
#
# for a in range(N):
#     stack=list(sys.stdin.readline().rstrip())
#     sum=0
#     while stack:
#         last=stack.pop()
#         if last == '(':
#             sum-=1
#         elif last==')':
#             sum+=1
#         if sum<0:
#             print('NO')
#             break
#     if sum==0:
#         print('YES')
#     elif sum>0:
#         print('NO')


#
# import sys
# N=int(sys.stdin.readline().strip())
# #N=int(input())
# for a in range(N):
#     #s=sys.stdin.readline().strip()
#     stack=list(sys.stdin.readline().strip())
#     #print(stack)
#     sum=0
# #    while stack:
#     for a in stack:
#         #last=stack.pop()
#         if a == '(':
#             sum+=1
#         elif a==')':
#             sum-=1
#         if sum<0:
#             print('NO')
#             break
#     # if sum==0:
#     #     print('YES')
#     # elif sum>0:
#     #     print('NO')
#     if sum>0:
#         print('NO')
#     elif sum==0:
#         print('YES')


# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
#     for i in s:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')

#4949번
# import sys
# #N=int(sys.stdin.readline())
# for line in sys.stdin.readlines():
#     line=list(line)
#     stack=[]
#     if len(line) == 1 & line[0] == '.':
#         break
#     for b in line:
#         if b =='(':
#             stack.append(1)
#         elif b==')':
#             if stack:
#                 if stack[-1]==1:
#                     stack.pop()
#                 else:
#                     #print('no')
#                     status='no'
#                     break
#             else :
#                 #print('no')
#                 status = 'no'
#                 break
#         elif b == '[':
#             stack.append(0)
#         elif b == ']':
#             if stack:
#                 if stack[-1]==0:
#                     stack.pop()
#                 else:
#                     #print('no')
#                     status = 'no'
#                     break
#             else :
#                 #print('no')
#                 status = 'no'
#                 break
#     if stack:
#         #status='no'
#         print('no')
#     if not stack and status!='no':
#         print('yes')
#     elif not stack and status=='no':
#         print('no')



# import sys
# N=sys.stdin.readlines()
# #N=input()
# print(N)
# #sum=0
# for line in N[:-1]:
#     print(line)
# # while True:
# #     line=input()
#     line=list(line)
#     stack=[]
#     if len(line) == 1 & line[0] == '.':
#         break
    # for b in line:
    #     if b =='(':
    #         stack.append(1)
    #     elif b==')':
    #         if stack:
    #             if stack[-1]==1:
    #                 stack.pop()
    #             else:
    #                 #print('no')
    #                 status='no'
    #                 break
    #         else :
    #             #print('no')
    #             status = 'no'
    #             break
    #     elif b == '[':
    #         stack.append(0)
    #     elif b == ']':
    #         if stack:
    #             if stack[-1]==0:
    #                 stack.pop()
    #             else:
    #                 #print('no')
    #                 status = 'no'
    #                 break
    #         else :
    #             #print('no')
    #             status = 'no'
    #             break
    # if stack:
    #     #status='no'
    #     print('no')
    # if not stack and status!='no':
    #     print('yes')
    # elif not stack and status=='no':
    #     print('no')


#short
# import sys
# lines = sys.stdin.readlines()
# for line in lines[:-1]:
#     stack = []
#     for t in line:
#         if t in '([':
#             stack.append(t)
#         elif t == "]":
#             if not stack or stack.pop() != '[':
#                 print('no')
#                 break
#         elif t == ')':
#             if not stack or stack.pop() != '(':
#                 print('no')
#                 break
#         elif t == '.':
#             if stack:
#                 print('no')
#             else:
#                 print("yes")



#short 2
# while True:
#     line = input()
#     if line == ".":
#         break
#     stack = []
#     status = 'yes'

# import sys
# N=sys.stdin.readlines()
# #for line in N[:-1]:
# for line in N:
#     line=list(line.rstrip())
#     stack=[]
#     status='yes'
#     if len(line) == 1 & line[0] == '.':
#     #if line==['.']:
#         break
#     for b in line:
#         if b =='(':
#             stack.append(1)
#         elif b==')':
#             if stack:
#                 if stack[-1]==1:
#                     stack.pop()
#                 else:
#                     #print('no')
#                     status='no'
#                     break
#             else :
#                 #print('no')
#                 status = 'no'
#                 break
#         elif b == '[':
#             stack.append(0)
#         elif b == ']':
#             if stack:
#                 if stack[-1]==0:
#                     stack.pop()
#                 else:
#                     #print('no')
#                     status = 'no'
#                     break
#             else :
#                 #print('no')
#                 status = 'no'
#                 break
#     if stack:
#         #status='no'
#         print('no')
#     if not stack and status!='no':
#         print('yes')
#     elif not stack and status=='no':
#         print('no')


# #
#     for j in bracket:
#         if j == "(" or j == "[":
#             bracket_stack.append(j)
#
#         elif j == ")":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "(":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break
#
#         elif j == "]":
#             if len(bracket_stack) == 0:
#                 answer = False
#                 break
#             if bracket_stack[-1] == "[":
#                 bracket_stack.pop()
#             else:
#                 answer = False
#                 break
#
#     if answer and not bracket_stack:
#         print("yes")
#     else:
#         print("no")

# #short
# import sys
# lines=sys.stdin.readlines()
# for line in lines[:-1]:
#     stack =[]
#     for t in line:
#         if t in '([':
#             stack.append(t)
#         elif t ==']':
#             if not stack or stack.pop()!='[':
#                 print('no')
#                 break
#         elif t == ')':
#             if not stack or stack.pop() != '(':
#                 print('no')
#                 break
#         elif t == '.':
#             if stack:
#                 print('no')
#             else:
#                 print("yes")
#
# #short
# while True:
#     s =input()
#     if s =='.':
#         break
#     stk=[]
#     temp=True
#     for i in s:
#         if i =='(' or i =='[':
#             stk.append(i)
#         elif i==')':
#             if not stk or stk[-1]=='[':
#                 temp=False
#                 break
#             elif stk[-1]=='(':
#                 stk.pop()
#         elif i==']':
#             if not stk or stk[-1]=='(':
#                 temp=False
#                 break
#             elif stk[-1]=='[':
#                 stk.pop()
#     if temp==True and not stk:
#         print('yes')
#     else:
#         print('no')
# #short
# import sys
# input = sys.stdin.readline
# while 1:
#     string = input().rstrip()
#     stack = []
#     true_flag = 1
#     for cha in string:
#         if cha == '(' or cha == '[':
#             stack.append(cha)
#         elif cha == ')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 true_flag = 0
#                 break
#         elif cha == ']':
#             if stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 true_flag = 0
#                 break
#     if string == '.':
#         break
#     print("yes" if true_flag and not(stack) else "no")


#1874

import sys
N=int(sys.stdin.readline().rstrip())
push=[]
rows=[]
#maxnum=[0]
maxnum=0
for a in range(N):
    num=int(sys.stdin.readline().rstrip())
    #maxnum.append(num)\
    if num>maxnum:
        maxnum=num
        #print(maxnum)

        # else: #없을때,
        # for b in range(max(maxnum),num)
    if num in push :
        print('d')
        if push[-1]==num:
            rows.append(push.pop())
            print('-')
            print('ddd')
        else:
            print('NO')
            break
            print('dddd')
        #print('wrong')
    #if not num in push:
    else:
        for b in range(maxnum, num):
            push.append(b + 1)
            print('+')
            print(push)

print(maxnum,push,rows)



        #rows.append(push.pop())
        #print('-')
        #print(push, rows, maxnum)

# 17298    #1.29 스터디 다시듣기
# import sys
# N=int(sys.stdin.readline())



