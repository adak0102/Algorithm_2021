#2739
# N=int(input())
# for a in range(9):
#     print(N,'*',a+1,'=',N*(a+1))
##short
# a=int(input())
# for i in range(1,10,1):
#     print(a,"*",i,"=",a*i)

#10950
# N=int(input())
# for i in range(N):
#     a, b=input().split()
#     print(int(a)+int(b))
#
# ##short
# import sys
# input()
# s=list(sum(map(int,n.split())) for n in sys.stdin)
#
# for n in s:
#     print(n)
# ###short
# for _ in range(int(sys.stdin.readline())):
#     print(sum(map(int,sys.stdin.readline().rstrip().split())))  #rstrip (오른쪽 공백/동일 문자제거)

#8393
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)
#
# #short
# n = int(input())
# print((n**2+n)//2)
# ##short
# print (sum(range(int(input())+1)))

#15552 ***
# import sys
# for a in range(int(sys.stdin.readline().rstrip())):
#     b,c= sys.stdin.readline().rstrip().split()
#     print(int(b)+int(c))
# #short #****#
# import sys
#
# IO = sys.stdin.read().split('\n')
#
# T = int(IO[0])
#
# del IO[0]
#
# for k in range(T):
#     A,B = IO[k].split()
#     IO[k] = (f"{int(A)+int(B)}\n")
#
# sys.stdout.write(''.join(IO))
#
# ##short
# import sys
# def add(T): # T = testcase
# 	for i in range(T):
# 		a, b = sys.stdin.readline().split()
# 		print( int(a) + int(b))
#
# a = sys.stdin.readline().split() # input Testcase
# add(int(a[0]))
# ###short
# n = int(input())
# for line in sys.stdin:
#     a,b = line.split()
#     print(int(a)+int(b))

#2741
# import sys
# for a in range(int(sys.stdin.readline().rstrip())):
#     print(a+1)
# ##short #**#
# n = range(1,int(input())+1)
# print('\n'.join(map(str,n)))  ## join : List를 특정구분자를 포함해 문자열로 변환하는 함수

#2742
# import sys
# N=int(sys.stdin.readline().rstrip())
#
# for a in range(N):
#     print(N-a)
#
# ##short
# n=int(input())
# print("\n".join(map(str, range(n, 0, -1))))

#11021
# N=int(input())
# for i in range(N):
#     print('Case #',i+1,': ',sum(map(int,input().split())),sep='')
#
# #short
# import sys
# num=int(input())
#
# for i in range(num):
#     a,b=map(int,sys.stdin.readline().split())
#     print("Case #%d:"%(i+1,a+b) # print('Case #%d: %d'%(i+1, a + b))

#11022
import sys
num=int(input())

for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d'%(i+1,a,b,a+b))

#short
import sys
input()
for i,line in enumerate(sys.stdin.readlines()):
    A,B=map(int,line.split())
    print(f"Case #{i+1}: {A} + {B} = {A+B}")

#2438

#2439

#10871
