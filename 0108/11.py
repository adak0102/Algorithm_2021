#2798 ****
# a,b= map(int,input().split())
# # print(a)
# # print(b)
# # number=[0 for _ in range(int(a))]
# list=list(map(int,input().split()))
#
# max=0
# # for i in range(a) : #[1,2,3,4,5] 5
# #     for j in range(a-1): #[2,3,4,5] 4
# #         for m in range(a-2): #[3,4,5] 3
# #             temp=list[i]+list[j+1]+list[m+2]
# #             if temp>max and temp<=b:
# #                 max=temp
# #                 print(list[i],list[j+1],list[m+2])
#
# for i in range(a) : #[1,2,3,4,5] 5         1   1  1    2  2   3
#     first=list[i]
#     for j in range(a-i-1): #[2,3,4,5] 4      2   3  4    3  4   4
#         second=list[i+j+1]
#         for m in range(a-i-j-2): #[3,4,5] 3    345 45 5    45 5   5
#             third=list[i+j+m+2]
#             temp=first+second+third
#             if temp>max and temp<=b:
#                 max=temp
#                 #print(first,second,third)
#
# print(max)
#
# #short
# def P(n,m,c):
#     t=set()
#     for i in range(n-2):
#         for o in range(i+1,n-1):
#             for p in range(o+1,n):
#                 s=c[i]+c[o]+c[p]
#                 if s <=m:
#                     t.add(s)
#                     break
#
#     return max([*t])  #?????
#
# print(P(*map(int,input().split()),list(sorted(map(int,input().split()))[::-1])))
# ##short
# import sys
# N,M=map(int,input().split())
# List=list(reversed(sorted(map(int,sys.stdin.readline().split()))))
# ansub=set()
# for i in range(N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             if List[i]+List[j]+List[k]==M:
#                 print(M)
#                 sys.exit()
#             else:
#                 if List[i]+List[j]+List[k]<M:
#                     ansub.add(List[i] + List[j] + List[k])
#                     break
# print(max(ansub))
# ###short
# N, M = map(int, input().split())
# cards = list(reversed(sorted(map(int, input().split()))))
# sumSet = set()
# blackjack = False
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             sum = cards[i] + cards[j] + cards[k]
#             if sum == M:
#                 blackjack = True
#                 break
#             elif sum < M:
#                 sumSet.add(sum)
#                 break
#         if blackjack:
#             break
#     if blackjack:
#         break
# if blackjack:
#     print(M)
# else:
#     print(max(sumSet))

#2231 X ##????왜 틀렷징?????##############
a=int(input())
##숫자리스트
list=[i for i in range(a+1)]
## 생성자 없을때 값
# for i in str(a):
#     max=a
#     max+=int(i)

##생성자함수
def d(n):
    for i in list:
        sumn = i
        for j in str(i):
            sumn+=int(j)
        if sumn==a:
            return i
    return 0
print(d(a))

#7568 OOO
# A=int(input())
# dungchi=[]
# for a in range(A):
#     dungchi.append(list(input().split()))
# rank=[1 for _ in range(A)]
# #print(dungchi)
# for i in range(A):
#     for j in range(A):
#         if dungchi[i][0]<dungchi[j][0] and dungchi[i][1]<dungchi[j][1]:
#             rank[i]+=1
#
# for i in rank:
#     print(i,end=' ')


##short
# num=int(input())
# val=[]
# for i in range(num) :
#     val.append(list(map(int,input().split())))
#
# for i in val :
#     rank=1
#     for j in val :
#         if i[0] < j[0] and i[1] < j[1]:
#                 rank += 1
#     print(rank,end=' ')


#1018  X #?????????
# a,b=map(int,input().split())
# text=[]
# #text=[ [0 for _ in range(a)] for _ in range(b) ]
#
# for i in range(a):
#     text.append(list(input()))
# cnt=0
# for i in range(a-1):
#     if text[i][1] == text[i + 1][1]:
#         if text[i][1]=='W':
#             text[i+1][1]='B'
#             cnt+=1
#         elif text[i][1]=='B':
#             text[i+1][1]='W'
#             cnt+=1
#     for j in range(b-1):
#         if text[i][j]==text[i][j+1]:
#             if text[i][j] == 'W':
#                 text[i][j+1] = 'B'
#                 cnt += 1
#             elif text[i][j] == 'B':
#                 text[i][j+1] = 'W'
#                 cnt += 1
# print(cnt)




#1436 X ##????????????????시간 초과?????????
a=input()
max=int(a+str(666))
list=[i for i in range(max+1)]
#print(list)

titlelist=[]
for i in list:
    if '666' in str(i):
        titlelist.append(i)
    
# print(titlelist)
print(titlelist[int(a)-1])
