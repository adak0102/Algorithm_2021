#1330
# A,B=input().split()
# A=int(A) ##**##
# B=int(B) ##**##
#
# if A>B :
#     print('>')
# elif A<B :
#     print('<')
# else:
#     print('==')

#9498
# a=int(input())
# if 90<=a<=100:
#     print('A')
# elif 80<=a<=89:
#     print('B')
# elif 70<=a<=79:
#     print('C')
# elif 60<=a<=69:
#     print('D')
# else:
#     print('F')
# #short
# a=int(input())
# if a>=90: print('A')
# elif a>=80: print('B')
# elif a>=70: print('C')
# elif a>=60: print('D')
# else: print('F')

#2753
# A=int(input())
# if A%400==0:
#     print('1')
# elif A%100!=0 and A%4==0:
#     print('1')
# else:
#     print('0')

##short
# a=int(input())
# if a%4==0 and a%100!=0 or a%400==0:
#     print(1)
# else:
#     print(0)

#14681
# a=int(input())
# b=int(input())
# if a>0 and b>0:
#     print(1)
# elif a>0 and b<0:
#     print(4)
# elif a<0 and b>0:
#     print(2)
# elif a<0 and b<0:
#     print(3)
#
# #SHORT
# if a>0:
#     print(1 if b>0 else 4)
# elif a <0:
#     print(2 if b>0 else 3)
#
# #
# x = int(input())
# y = int(input())
#
# if y > 0:
# 	if x > 0:
# 		print(1)
# 	else:
# 		print(2)
# else:
# 	if x > 0:
# 		print(4)
# 	else:
# 		print(3)

#2884
# hour,minut=input().split()
# hour=int(hour)
# minut=int(minut)
#
# if minut>=45 :  #=***
#     print(hour,minut-45)
# elif minut<45 and hour==0:
#     print(23,minut+15)
# else:
#     print(hour-1,minut+15)

#short# ****
# a,b=map(int,input().split());x=a*60+b-45;print(x//60%24,x%60)

