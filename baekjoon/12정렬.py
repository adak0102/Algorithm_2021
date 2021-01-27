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
# import sys
# N=int(sys.stdin.readline())
# li=[ int(sys.stdin.readline().rstrip()) for _ in range(N)]
#
# # N,*a = sys.stdin.read() #readlines()
# # print(N,a)
#
# print(round(sum(li)/len(li)))
# sor=sorted(li)
# print(sor[len(li)//2])
# #li.sort()
# #print(li[len(li]//2])
#
# #딕셔너리로 만들고 출력
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
# #print(di)
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
###short 확인 필요 #https://dojang.io/mod/page/view.php?id=2286 #map 다시 읽고 정리####
###################################################################################


#11650
import sys
N=int(sys.stdin.readline())   #sys.stdin 은 전부 읽어오는거 인듯  #IO = sys.stdin.read().split('\n')
                              #sys.stdin() 틀림 -> sys.stdin

#li=[[0,0]]*N # 이러면 왜 안되는지???
#list comprehension 이랑 zip함수

li=[[ _ for _ in range(2)] for _ in range(0,N)]
# for a in range(N):
#     li[a][0],li[a][1] = input().rstrip().split()

for a in range(N):
    li[a][0],li[a][1] = sys.stdin.readline().split()

li.sort()

for a in range(N):

    print(li[a][0],li[a][1])

###Again###
# left=[]
# right=[]
left={}
right={}
for i in range(N):
    a,b= map(int, sys.stdin.readline().rstrip().split())
    left[i]=a
    right[i]=b

if




    # left.append(a)
    # right.append(b)

#딕셔너리 사용
# dic={}
# for i, j in enumerate(left):
#     dic[i]=j








#11651

#1181
# import sys
# N=int(sys.stdin.readline())
# li=[]
# for a in range(N):
#     li.append(sys.stdin.readline().rstrip())
#
# li.sort()
# print(li)
#10814


#값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 합니다.