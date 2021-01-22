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


#2751
#시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다.
# 예를 들면 병합 정렬, 힙 정렬 등이 있지만, 어려운 알고리즘이므로 지금은 언어에 내장된 정렬 함수를 쓰는 것을 추천드립니다.
# N=int(input())
# list=[]
# for a in range(N):
#     list.append(int(input()))
# print(list)

what=[3,4,1,6,2,9]


# def merge (sub1:list, sub2: list, L:list) :
#     i=j=k=0 #checking if any element is left
#     while i<len(sub1) and j<len(sub2):
#         if sub1[i]<=sub2[j]:
#             L[k]=sub1[i]
#             i+=1
#         else:
#             L[k]=sub2[j]
#             j+=1
#         k+=1
#
# def merge_sort(L:list):
#     if len(L) <= 1: #conditional statements
#         return  L  #Base case
#     else:
#         mid=len(L)//2
#         subL1,subL2=L[:mid],L[mid:] #Divide the list into 2 sublists
#         merge_sort(subL1)   #Recursive call ofr sublist 1,2
#         merge_sort(subL2)
#         merge(subL1,subL2,L) #merge 2 sorted sublists
#
# merge_sort(what)
# print(what)
##
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
# def merge_sort(L:list)->None:
#     if len(L)<=1:
#         return
#     else:
#         mid=len(L)//2
#         subL1,subL2=L[:mid],L[mid:]
#         merge_sort(subL1)
#         merge_sort(subL2)
#         merge(subL1,subL2,L)


# import timeit
# start=timeit.default_timer()
##l=[1,48,-3,225,-6,8,5,90,45,3]
# l=[i for i in range(1000)]
# merge_sort(l)
# print(l)
# print('time: %f' %(timeit.default_timer()-start))
##

def Mergesort(L:list):
    ## recursion Error : 재귀 너무 많이 함
    if len(L)<=1:
        return
    mid=len(L)//2
    L1=L[:mid]
    L2=L[mid:]
    #return Merge(Mergesort(L1),Mergesort(L2))
    Merge(Mergesort(L1), Mergesort(L2))

def Merge(L1:list,L2:list):
    listsum=[]
    i,j=0,0
    while i<=len(L1) or j<=len(L2):
        if L1[i]>L2[j]:
            listsum.append(L2[j])
            j+=1
        elif L1[i]<L2[j]:
            listsum.append(L1[i])
            i+=1
    return listsum

Mergesort(what)
print(what)

#
# Mergesort(list)

    # for i in range(len(L1)):
    #     for j in range(len(L2)):
    #         if L1[i]<L2[j]:
    #





#10989
#수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다


#2108

#1427

#11650

#11651

#1181

#10814
#값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 합니다.