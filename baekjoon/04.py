#10952
# while True:
#     a, b = map(int, input().split())
#     if a==0 and b==0:
#         break
#     else:
#         print(a + b)
# #short
# import sys
# for k in sys.stdin:
#     a,b=map(int,k.split())
#     if a!=0 and b!=0:
#         print(a+b)
# ##short
# import sys
#
# while True:
# 	a, b = map(int, sys.stdin.readline().split())
# 	if (a == 0 and b == 0):
# 		break
# 	print(a+b)


#10951 #***#
# import sys
# #read=sys.stdin.read()
# for k in sys.stdin:
#         print(sum(map(int,k.split())))

# while True:
#     print(sum(map(int,input().split())))
# 런타임 에러

#short
# while True:
#     try :
#         a,b= map(int,input().split())
#         #a,b=map(int,sys.stdin.readline().split())
#     except:
#         break
#     print(a+b)

# ##short #???
# import sys
# [print(eval("+".join(line.split()))) for line in sys.stdin]


#1110
N=(input())
count=0
while True:
    if int(N)<10:
        N[0]=0
        N[1]=N

    K=int(N[0])+int(N[1])+int(N[1])*10
    count+=1

    if K==int(N):

        break
print(count)