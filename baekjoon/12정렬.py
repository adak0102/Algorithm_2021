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
##

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

##SHORT
        #추가하기#내장함수 사용


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


#2108

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

###################################################################################
###short 확인 필요 #https://dojang.io/mod/page/view.php?id=2286 #map 다시 읽고 정리####
###################################################################################


#11650

#11651

#1181

#10814
#값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 합니다.