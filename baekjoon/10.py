#10872 XO
# a=int(input())
# def factorial(n):
#   if n==0:
#       return 1
#   return n * factorial(n - 1) ###함수 리턴값 설정!!!!****
# print(factorial(a))
#
# #오답
# a=int(input())
# def factorial(n):
#     n * factorial(n - 1)
#     if n==0:
#         return 1
# print(factorial(a))

#10870
# a=int(input())
# def Pibonacchi(a):
#     if a==0:
#         return 0
#     elif a==1:
#         return 1
#     return Pibonacchi(a-1)+Pibonacchi(a-2)
#
#
# print(Pibonacchi(a))

#2447 X
def star(n):
    if n==3:
        return('***\n* *\n***')
    return (star(n/3)*3,'\n',star(n/3),n/3*' ',star(n/3),'\n',star(n/3)*3)

print(star(27))

#11729 X

def hanoi(n):
    if n==1:
        return 1
    return hanoi(n-1)+hanoi(n-1)+1

def hanoicnt(n):
