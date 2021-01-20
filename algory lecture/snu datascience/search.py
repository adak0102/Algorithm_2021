# Algorithm: A recipe for computers to follow (logical steps)
# Program: An instruction set in programming languages for a computer to
#                 understand and put an algorithm to practice

# Linear Search
# # Find if a target value exists in a list
# # To do this, search from the first item to the last item sequentially (linear search)
# # If the target value exists, return the index where the value first occurs
# # Otherwise, return -1
#
#(1)
def linear_search_while(L:list, value: Any)-> int:
    i=0
    while i<len(L) and L[i]!=value:
        i+=1
    if i==len(L):
        return -1
    else:
        return i

#(2) While Loop with Sentinel at the end of the list
def linear_search_sentinel(L:list, value:Any)->int:
    L.append(value)  #Add the Sentinel
    i=0
    while L[i]!=value:  #Sentinel 덕분에 / this condition is enough, No needs to do (i < len(L)) every time
        i+=1
    L.pop() #remove sentinel
    if i==len(L): #while 문 나올때, L 리스트와 길이 같으면
        return -1
    else:
        return i
#(3) for Loop
def linear_search_for(L:list,value:Any)->int:
    for i in range(len(L)):
        if L[i]==value:
            return i
    return -1

##Measure Time Complexity
import time
t_start=time.perf_counter()
#<<Your Algorithm>>
t_end=time.perf_counter()
return (t_end - t_start)*1000.0

# Binary Search >> Sorting 된 상태에서 사용가능
# Idea: Evaluate the middle of the sorted list and removes half of candidate entries
# Linear search: one evaluation removes one candidate entry
# Binary search: one evaluation removes half of candidate entries

def binary_search(L:list, v:Any)->int:
    start, end = 0, len(L)-1
    while start!=end+1:
        mid=(start+end)//2
        if L[mid]<v:
            start=mid+1
        else:
            end=mid-1
        if start<len(L) and L[start]==v:
            return start
    else:
        return -1

