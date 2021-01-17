#11654
# A=input()
# print(ord(A))
#
# #short
# print(ord(input()))

#10809 알파벳 찾기 XXXOOO
# 오답
# for a in range(64:89):
# print(range(64:89))   #97-122
#오답
# for i in range(97,123):
#     print(chr(i), end=' ')

#해답
# A=input()
# for i in range(97,123):
#     print(A.find(chr(i)),end=' ')
#
#     # if chr(i) in list(A):
#     #     print(A.find(chr(i)))#
#     # else:
#     #     print(-1)
#
##short
# string = input()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabet:
#     print(string.find(i), end = ' ')

###short
# s = input()
# ans = [-1,]*26 ## list 원소 -1 26개
# k = 0
# for c in s:
#     index = ord(c)-97
#     if ans[index] == -1:
#         ans[index] = k
#     k += 1
# for d in ans:
#     print(d, end=' ')

#11720#다른 방법 생각해보기
# N=int(input())
# str=list(input())
# print(sum(map(int,str)))

# 2675
# A=int(input())
#
# for i in range(A):
#     a,b=input().split()
#     blist=list(b)
#     for f in blist:
#         print(f*(int(a)),end='')
#     print() #**************# 다음 출력**
#
#
# A=int(input())
# for i in range(A):
#     a,b=input().split()
#     for f in b:
#         print(f*(int(a)),end='')
#     print() #**************# 다음 출력**

#1157 XXXOOO!!!!!!!!!!!!
# word=input()
# word=word.upper()
#
# blank={}
# # for a,b in enumerate(word):
# #     print(a,':',b)
# for i in word:
#     blank[i] = 0
#
# for key in blank.keys():
#     for w in word:
#         if key==w:
#             blank[key]+=1
#
# maxcnt=0
# maxkey=0
# for key,value in blank.items():
#     if blank[key]>maxcnt: #value==blank[max(blank)]:
#         maxcnt=blank[key]
#         maxkey=key
#
# smcnt=0
# for key,value in blank.items():
#     if value==maxcnt:
#         smcnt+=1
#
# if smcnt>1:
#     print('?')
# else:
#     print(maxkey)

##short !!!!!!!!!!!!##################
# #1 *****
# s,a=input.lower(),[]
# for i in range(97,123):
#     a.append(s.count(chr(i)))
# print('?'if a.count(max(a))>1 else chr(a.index(max(a))).upper())
# #2
# n=input()
# n=n.upper()
# alpa="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# result=[]
# for i in alpa:
#     result.append(n.count(i))
# if result.count(max(result))>1:
#     print('?')
# else:
#     print(alpa[result.index(max(result))])
# #3
# word=input().upper()
# abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# key=0
# count=0
# for a in abc:
#     temp=word.count(a)
#     if count<temp:
#         count=temp
#         key=a
#     elif temp==count:
#         key='?'
# print(key)
#
#
# #4
# s = str(input())
# S = s.upper()
#
# chrDict = list()
# for i in range(65, 91):
#     chrDict.append(S.count(chr(i)))
#
# maxNum = max(chrDict)
# if chrDict.count(maxNum) == 1:
#     alphabet = chr(chrDict.index(maxNum)+65)
#     print(alphabet)
# else:
#     print("?")
#####################################


#1152
# w=input().strip()
# s=w.split()
# #print(s)
# print(len(s))

#short
# import sys
# s = sys.stdin.read().strip()
# if not s:
#     print("0")
# else:
#     print(len(s.split(" ")))
## short ***
# s = input().strip()
# print(s.count(' ') + 1 if s else 0)

#2908
# a,b=input().split()
# a=list(a)
# b=list(b)
#
# newa=[0 for _ in range(len(a))]
# newb=[0 for _ in range(len(b))]
# for i in range(len(a)):
#     newa[i]=a[len(a)-i-1]
#
# for j in range(len(b)):
#     newb[j]=b[len(b)-j-1]
#
# #print(newa,newb)
# #print("".join(newa))
# print(max(int("".join(newa)),int("".join(newb))))
#
# #쉽게...short
# a, b =input().split()
#
# def reading(k):
#     k = k[::-1]
#     return int(k)
#
# print(max([reading(a),reading(b)]))
# ##short
# print(max([int(i[::-1]) for i in input().split()]))
# #
# A,B = input().split()
# print(max(A[::-1], B[::-1]))
# #
# x, y = input().split()
# print(max(int(x[::-1]), int(y[::-1])))
# #
# N = input().split()
# N = [int(i[::-1]) for i in N]
# print(max(N))

#5622 XXX
#(A)65-(Z)90 656667-678->2 686970-91011->3 717273->4
# number=input()
# l=list(number)
# for i in l :
#     (ord(i)-59)/3
#
# print(ord(number))



#2941
A=input()
list=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0

for i in list:
    if i in A:
        cnt+=1

print(cnt)


#1316






