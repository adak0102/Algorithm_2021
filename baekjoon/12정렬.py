#2750 (삽입정렬)
# def insertionsort(L:list):
#     sort=[L[0],]
#     for i in range(1,len(L)):
#         insert_sort(L[i],sort)
#
#     for a in sort:
#         print(a)
#
# def insert_sort(new:int,L:list): #(4,[2,3,5])
#     i=0
#     for a in range(len(L)):
#         if L[i]<new:  #2<4 i=1 #
#             i+=1
#         else: #L[i]>new:
#             pass
#     L.insert(i,new)
#
# N=int(input())
# list=[]
# for a in range(N):
#     list.append(int(input()))
# insertionsort(list)

#[Other solutions] 1~
#deport
# N=int(input())
# list=[]
# for a in range(N):
#     list.append(int(input()))

#(1)SNU
# def insertion_sort(L:list)->None:
#     i=1 #sort는 0부터 시작
#     while i<len(L): #반복문은 while로!!
#         insert_sort(L,i)
#         i+=1
#
# def insert_sort(L:list,last_idx:int):
#     value=L[last_idx]
#     i=last_idx
#     while i>0 & L[i-1]>L[i]:
#         i-=1
#     del L[last_idx]
#     L.insert(i,value)

#(2)Insert Sort
# for i in range(1, len(list)):
#     while (i>0) & (list[i] < list[i-1]):
#         list[i],list[i-1]=list[i-1],list[i]
#         i-=1

#(3)Bubbel Sort
# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i]<list[j]:
#             list[i],list[j]=list[j],list[i]
#
# for n in list:
#     print(n)

#(4) other
# list=sorted(list)
#(5)
# list.sort()
# #insert
# for i in range(1,len(list)):
#     while i>0 and list[i]<list[i-1]:
#         list[i-1],list[i]=list[i],list[i-1]
#         i-=1

#short Baekjoon
# import sys
# N=int(sys.stdin.readline().strip())
# s=[0]*int(N)
# for i in range(N):
#     s[i]=int(sys.stdin.readline().strip())
# s.sort()
#
# s=list(map(str,s))
# print('\n'.join(s)) #sys.stdout.write("\n".join(map(str, numbers)))

#2751 (MERGE SORT)
#시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다.
# 예를 들면 병합 정렬, 힙 정렬 등이 있지만, 어려운 알고리즘이므로 지금은 언어에 내장된 정렬 함수를 쓰는 것을 추천드립니다.
# N=int(input())
# list=[]
# for a in range(N):
#     list.append(int(input()))

## SNU CORRECT
# N=int(input())
# list=[]
# for a in range(N):
#     list.append(int(input()))
#
# def merge(sub1: list, sub2: list, L: list) -> None:
#     i = j = k = 0
#     while i < len(sub1) and j < len(sub2):
#         if sub1[i] <= sub2[j]:
#             L[k] = sub1[i]
#             i = i+1
#         else:
#             L[k] = sub2[j]
#             j = j+1
#         k = k+1
#
#     while i < len(sub1):
#         L[k]=sub1[i]
#         i=i+1
#         k=k+1
#     while j <len(sub2):
#         L[k]=sub2[j]
#         j=j+1
#         k=k+1
#
# def merge_sort(L:list)->None:
#     if len(L)<=1:
#         return L
#     else:
#         mid=len(L)//2
#         subL1,subL2=L[:mid],L[mid:]
#         merge_sort(subL1)
#         merge_sort(subL2)
#         merge(subL1,subL2,L)
#
# merge_sort(list)
#
# for a in list:
#     print (a)

# import timeit
# start=timeit.default_timer()
##l=[1,48,-3,225,-6,8,5,90,45,3]
# l=[i for i in range(1000)]
# merge_sort(l)
# print(l)
# print('time: %f' %(timeit.default_timer()-start))

# my wrong
# def Mergesort(L:list):
#     ## recursion Error : 재귀 너무 많이 함
#     if len(L)<=1:
#         return L
#     mid=len(L)//2
#     L1=L[:mid]
#     L2=L[mid:]
#     #return Merge(Mergesort(L1),Mergesort(L2))
#     Merge(Mergesort(L1), Mergesort(L2))
#
#
# def Merge(L1:list,L2:list):
#     listsum=[]
#     i,j=0,0
#     while i<len(L1) and j<len(L2):
#     #while i!=len(L1) and j!=len(L2):
#         if L1[i]<=L2[j]:
#             listsum.append(L1[i])
#             i+=1
#         else:
#         #elif L1[i]>=L2[j]:
#             listsum.append(L2[j])
#             j+=1
#     while i < len(L1):
#         listsum.append(L1[i])
#         i+=1
#     while j < len(L2):
#         listsum.append(L2[j])
#         j+=1
#     return listsum

# Mergesort(list)
# print(list)

#short 1-3
# ##SHORT(1)
# from sys import stdin, stdout
# input()
# arr=sorted(map(int,stdin.read().split()))
# stdout.write('\n'.join(map(str,arr)))
#
# ##SHORT(2)
# import sys
# n=int(sys.stdin.readline())
# a=sorted(list(map(int,sys.stdin.read().split())))
# print('\n'.join(map(str,a)))
#
# ##short(3)
# import sys
# n,*s= map(int,sys.stdin.read().split())
#
# print(*sorted(s),sep='\n')

#10989 (COUNTING SORT)
#수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다
#(첫단)
# N=int(input())
# list=[]
# for a in range(N):
#     list.append(int(input()))

##count sort 구현
# countsort(1)
#https://debuglog.tistory.com/68
# def countsort(arr,k):  #k는 max...#k는 각요소가 몇개씩 들어있는 지를 담을 c배열을 k크기로 초기화 해줌
#     c=[0]*k
#     sorted_arr = [0]*len(arr)
#
#     for i in arr:
#         c[i]+=1
#
#     for i in range(1,k):
#         c[i]+=c[i-1]
#
#     for i in range(len(arr)):
#         sorted_arr[c[arr[i]]-1]=arr[i]
#         c[arr[i]]-=1
#
#     return sorted_arr
#
# print(countsort(list, max(list)))
#

##https://zetawiki.com/wiki/BOJ_10989_%EC%88%98_%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0_3
#countsort(2)
# MAX=10000
# a = [0]*MAX
# f = open(0)
# f.readline()
# for i in f:
#     a[int(i)]+=1
# for i in range(MAX):
#     print("%s\n" % i*a[i], end="")

##
#countsort(3)
# import sys
# N=int(sys.stdin.readline())
# li=[0]*1001
# for i in range(N):
# 		a=sys.stdin.readline()
# 		li[int(a)]+=1
# for j in range(1,1001):
# 		if li[j] >= 1:
# 				for k in range(li[j]):
# 						print(j)

##
#countsort(4)
# def couting_sort(A, k):
#     B = [0] * len(A)
#     C = [0] * (k + 1)
#
#     for i in range(len(A)):  # 각 element가 몇개있는지 C에 저장한다
#         C[A[i]] += 1
#
#     for i in range(1, len(C)):  # C를 누적값으로 바꾼다
#         C[i] += C[i - 1]
#
#     for i in range(len(A)):  # C를 indexing해서 B에 저장한다
#         B[C[A[i]] - 1] = A[i]
#         C[A[i]] -= 1
#
#     return B


# counting_number = [1, 0, 3, 1, 0, 2, 5, 2, 1, 4]
# print(counting_number)
# count = couting_sort(counting_number, max(counting_number))
# print(count)

#countsort(메모리 통과 5)
# import sys
# li=[0 for _ in range(10001)]
# N=int(sys.stdin.readline())
#
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     li[num]+=1
#
# for i in range(1,10001):
#     count=li[i]
#     for _ in range(count):
#         print(i)

# 메모리 초과 문제 읽어보기 (6)
# https://wook-2124.tistory.com/403

#(끝단)
# print(max(list))
# count = couting_sort(list, max(list))
# for a in count:
#     print(a)

##short(1)
# f=open(0)
# f.readline()
# li=[0]*10001
# for line in f:
#     li[int(line)]+=1
# for i in range(1, 10001):
#     print(f'{i}\n'*li[i], end='')

#2108
#지저분
# # li=[ int(sys.stdin.readline().rstrip()) for _ in range(N)]
# #
# # N,*a = sys.stdin.read() #readlines()
# # print(N,a)
# #
# #
# # li.sort()
# # print(li[len(li]//2])
#
# #dic
# dic={}
# for a in range(N):
#     new=int(sys.stdin.readline().rstrip())
#     if new in dic.keys():
#         dic[new]+=1
#     else:
#         dic[new]=1
#
#
# #산술평균
# print(sum(dic.keys())/len(dic))
# #중앙값
# print(dic[len(dic.keys())//2])
# #범위
# print(max(dic.keys())-min(dic.keys()))
# #최빈값
# sordic=sorted(dic.items(), key=lambda x:x[1])
#
# #많은 수인 값
# most=sordic[-1]
# print(most)
# m=most[1]
#
# #키값 꺼내기
# result=[]
# for a ,b in dic.items():
#     if b==m:
#         result.append(int(a))
# print(result)
# #result=dic.keys(m)
# print(result)
# result=sorted(result)
# if len(result)>=2:
#     print(result[1])
# else :
#     print(result[0])
#
# 시간초과 풀이 (XXX)
# import sys
# N=int(sys.stdin.readline().rstrip())
# ## 다시
# li=[]
# for a in range(N):
#     li.append(int(sys.stdin.readline().rstrip()))
# print(li)
# #산술평균
# print(round(sum(li)/len(li))) #소수점 이하 첫자리 반올림
#
# #중앙값
# li.sort()
# print(li[len(li)//2])

#최빈값 (XXXX)
#변수 for문 밖!!!
# value=[]
# ma = 1
# for a in li:
#     if a >= ma:
#         ma
#         value.append(a)
# value.sort()
#
# print(value[1] if len(value)>=2 else print (value[0]))
                        # if len(value)>=2 :
                        #     print(value[1])
                        # else :
                        #     print(value[0])
#
#
#
# #범위
# print(li[-1]-li[0]) #**#
#                         #print(max(li)-min(li))


# di={}
# for a in li:
#     if a in di.keys() :
#         di[a]+=1
#     else:
#         di[a] = 1
#
# ma=max(di.values())
# fre={}
# for a in di.keys():
#     if di[a]==ma:
#         fre.append(fre[a])
# if len(fre)>1:
#     print(fre[1])
# else: print(fre[0])
#print(di)

# print(round(sum(li)/len(li)))
# sor=sorted(li)
# print(sor[len(li)//2])
#
# print(max(di))
#
# print(max(li)-min(li))





#1427 소트인사이드
# import sys
# N=sys.stdin.readline().rstrip()
# li=[]
# for a in N:
#     li.append(int(a))
# #map(int,list)
#
# li.sort(reverse=True)
# li=list(map(str,li))  #꼭 list 에 다시 넣어서 써야함 map 함수는!!
# #print(li)
# new=''.join(li)
# print(new)

# for a in list:
#     print(a,end='')

#short 5
# ##short(1)
# print(''.join(sorted(input())[::-1]))
# #short(2)
# print(''.join(sorted(input(),reverse=True)))
# #short(3)
# n=input()
# print(''.join(sorted(n,reverse=True)))
# #short(4)
# import sys
# print(''.join(sorted(sys.stdin.readline().rstrip())[;;-1]))
# #short(5)
# p=list(map(int,input()))
# p.sort(reverse=True)
# p=list(map(str,p))
# print(''.join(p))

###################################################################################
###short 확인 필요 #https://dojang.io/mod/page/view.php?id=2286 #map 다시 정리####
###################################################################################


#11650 (0)
# ###Again###
# # left=[]
# # right=[]
# left={}
# right={}
# for i in range(N):
#     a,b= map(int, sys.stdin.readline().rstrip().split())
#     left[i]=a
#     right[i]=b
# #딕셔너리 밸류값으로 sort
#
# for i in range(N):
#     if left[i]

    # left.append(a)
    # right.append(b)

#내꺼 XXXXX 왜..ㅠ?
# import sys
# N=int(sys.stdin.readline())
# #초기화 리스트
# li=[[ _ for _ in range(2)] for _ in range(0,N)]
# for a in range(N):
#     li[a][0],li[a][1] = sys.stdin.readline().split()
# li.sort() #[(1,2),(2,3)]
# for a in range(N):
#     print(li[a][0],li[a][1])
#
# #다시 (0)
# import sys
# N=int(sys.stdin.readline().rstrip())
#
# li=[]
# for a in range(N):
#     ####li = []#### FOR 문안에 LIST xxx 실수xxx
#     new = list(map(int, sys.stdin.readline().rstrip().split()))
#     li.append(new)
#
# li.sort(key = lambda x : (x[0],x[1]))
# for a in li:
#     print( a[0], a[1])

##insert 나 remove는 시간이 많이 걸림 o(n)만큼 걸린다. 리스트는 인덱스..!!

#short (검토 필요)
# # https://www.acmicpc.net/problem/11650

from sys import stdin, stdout

stdout.write(
    '\n'.join(
        f'{v // 1000000 - 100000} {v % 1000000 - 100000}'
        for v
        in sorted(
            (int(line.split()[0])+100000) * 1000000
            + int(line.split()[1])+100000
            for line in stdin.read().splitlines()[1:]
        )
    ) + '\n'
)


#Short

# import sys
# input = sys.stdin.readline
# coords = [input() for _ in range(int(input()))]
# coords = sorted(coords, key=lambda coord: (int(coord.split()[0]),int(coord.split()[1])))
#
# print(''.join(coords))

#short 2
# import sys
# input=sys.stdin.readline
# N=int(input())
# li=list()
# for _ in range(N):
#     x,y=map(int,input().split())
#     li.append((x,y))
# print("\n".join(f"{n[0]} {n[1]}" for n in sorted(li)))

#short 3 (검토 X)
# from sys import stdin, stdout
#
# n = int(stdin.readline())
# ans = []
# for _ in range(n):
#     ans.append(tuple(map(int, stdin.readline().split())))
#
# stdout.write('\n'.join(f"{i[0]} {i[1]}" for i in sorted(ans)))



# 11651 (0)
#(0)
# import sys
# N=int(sys.stdin.readline().rstrip())
# li=[]
# for a in range(N):
#     ####li = []#### FOR 문안에 LIST xxx 실수xxx
#     new = list(map(int, sys.stdin.readline().rstrip().split()))
#     li.append(new)
#
# li.sort(key = lambda x : (x[1],x[0]))
# for a in li:
#     print( a[0], a[1])

#SHORT 1 (*****) # 왜 [[],[]]은 안되고 [(),()]은 되는지 ?
# import sys
# input=sys.stdin.readline
# N=int(input())
# li=list()
# for _ in range(N):
#     x,y=map(int,input().split())
#     li.append((y,x))
# print("\n".join(f"{n[1]} {n[0]}" for n in sorted(li)))


#SHORT 2 (나중)
# from sys import stdin, stdout
#
# stdout.write(
#     '\n'.join(
#         f'{v % 1000000 - 100000} {v // 1000000 - 100000}'
#         for v
#         in sorted(
#             (int(line.split()[1])+100000) * 1000000
#             + int(line.split()[0])+100000
#             for line in stdin.read().splitlines()[1:]
#         )
#     ) + '\n'
# )


#1181 (3. XXX)
# import sys
# N=int(sys.stdin.readline())
# li=[]
# for a in range(N):
#     li.append(sys.stdin.readline().rstrip())
# li.sort()
# print(li)

#dic={}
# 딕셔너리로 input 받기

# 1. 키값 숫자로
# for a in range(N):
#     new=sys.stdin.readline().rstrip()
#     if len(new) not in dic.keys():
#         dic[len(new)] = new
#         #dic.setdefault(len(new))
#         #dic[len(new)]=[]  #dic[len(new)]=[]
#     else :
#         dic[len(new)]=dic[len(new)],new

# 2. 키 값 단어로
# for a in range(N):
#     new=sys.stdin.readline().rstrip()
#     if len(new) not in dic:
#         dic[len(new)]=new
#     elif len(new) in dic and new not in dic[len(new)] :
#         valuli=[]
#         # print(dic[len(new)])
#         # valuli=valuli.append(dic[len(new)])
#
#         valuli=dic[len(new)]
#         valuli.append(new)
#         #valuli.append(dic[len(new)])
#         print(valuli)
#         dic[len(new)]=valuli

# 3. 다시 => 답 나오는데, 시간초과로  XXXX
# # {단어 명 : 길이} 로 딕셔너리
# dic={}
# for a in range(N):
#     new=sys.stdin.readline().rstrip()
#     if new not in dic:
#         dic[new]=len(new)
#
# #단어 길이 먼저, 단어 명 순위로 sort =? 결과 왜 튜플로 나오징
# print(type(dic[0]))
# dic=sorted(dic.items(), key=lambda x:(x[1],x[0]))
#
# #결과 하나씩
# for a in range(len(dic)):
#     print(dic[a][0])

#10814 XXXXX (왜??????)
# import sys
# N=int(sys.stdin.readline())
# li=[]
# for a in range(N):
#     x=(a,sys.stdin.readline().rstrip().split())
#     li.append(x)
#
# li.sort(key=lambda x : (x[1][0],x[0]))
#
# for a in range(len(li)):
#     print((li[a][1])[0],(li[a][1])[1])

####print('\n'.join(f"n[0] n[1]" for n in sorted(li)))

#값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 합니다.