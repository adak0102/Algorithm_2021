#10869
# a,b=input().split()
# A=int(a)
# B=int(b)
# print(A+B,A-B,A*B,A//B,A%B,sep='\n')

#10430
    #A,B,C=int(input().split()) #???
# A,B,C=input().split()
# A=int(A)
# B=int(B)
# C=int(C)
# print((A + B) % C,((A % C) + (B % C)) % C,(A*B) % C,((A % C)*(B % C)) % C, sep='\n')


#2588 내코드
# A=int(input())
# B=int(input())
# C=B%10  #374
# E=B//100
# D=(B-E*100-C)//10
# print(A*C)
# print(A*D)
# print(A*E)
# print(A*(C+10*D+100*E))

#참고
# a=int(input())  #234
# b=list(map(int,list(input())))  #['234']
# c=input().split()  #['234']
# print(a,b,c)
# d=list(input())
# print(d)

# ## 2588 다른 풀이
# a = int(input())
# b = list(map(int,list(input())))
# for i in range(3):
# 	print(a*b[2-i])
# print(a*(100*b[0]+10*b[1]+b[2]))