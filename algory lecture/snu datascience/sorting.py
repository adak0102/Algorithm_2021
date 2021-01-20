#Selection sort
#Find the minumum value of the unsorted list
#and swap it with the leftmost entry : unsorted start form [0]

def selection_sort(L:list)->None:
    i=0
    while i<len(L):
        #Find the index of the smallest item in L[i:];smallest
        smalleset=find_min(L,i)
        L[i],L[smalleset]=L[smalleset],L[i]
        i+=1

def find_min(L:list, start_idx:int)->int:
    smallest=start_idx #initialize smallest
    i=start_idx+1 #update smallest
    while i <len(L):
        if L[i]<L[smalleset]:
            smalleset=i
        i+=1
    return smalleset
#Time Complexity : N+(N-1)+(N-2)+(N-3)+...+1= N(N+1)/2 (func find_min needs to look up (N+1-i) items


#Insertion sort
#Insert the leftmost item of the unsorted list to the proper location of the sorted list
#sorted start form [0], unsorted start from [1] # 이미 sorted된 리스트에서 어디에 들어가야할지 열심히 찾는데 시간 사용

def insertion_sort(L:list)->None:
    i=1 #unsorted 1번, sorted 0번부터 시작!
    while i<len(L):
        #insert L[i] to the proper location of L[:i]
        insert(L,i)
        i+=1


def insert(L:list, last_idx:int)->None:
    value=L[last_idx] #set the target value
    i=last_idx  #set the insert location
    while i>0 and L[i-1] >= value:
        i-=1
    del L[last_idx] #원래 있던것 delete
    L.insert(i,value) #insert

#Time Complexity
#At i-th iteration, its inner loop(func insert) needs to look up (i+1)/2 items on average
# 1+1.5+2+2.5+...+(N-1)/2 + N/2 (when N=len(c))=N(N+1)/4-1/2
#twice faster than selection sort : find_min needs to look up the whole list, insert() needs to look up only half on average


#Merge sort
#1. Divide the whole task into two sub-lists(parts)
#2.sort the left sublist & the right sublist seperately by using merge sort
#3.merge the two sorted sublist in a sorted way

def merge_sort(L:list)->None:
    if len(L) <= 1: #conditional statements
        return L   #Base case
    else:
        mid=len(L)//2
        subL1,subL2=L[:mid],L[mid:] #Divide the list into 2 sublists
        merge_sort(subL1)   #Recursive call ofr sublist 1,2
        merge_sort(subL2)
        merge(subL1,subL2,L) #merge 2 sorted sublists

def merge (sub1:list, sub2: list, L:list) -> None:
    i=j=k=0 #checking if any element is left
    while i<len(sub1) and j<len(sub2):
        if sub1[i]<=sub2[j]:
            L[k]=sub1[i]
            i+=1
        else:
            L[k]=sub2[j]
            j+=1
        k+=1

#Time complextiy : N*log2_N
#list 개수 : N
