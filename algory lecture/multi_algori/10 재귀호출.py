# def recursion():
#     print('나불렀음?')
#     recursion()
#
# recursion()


#함수는 호출시 스택사용 : a-b-c-d 호출  돌아갈때 d-c-b-a
#재귀함수 부르고부르고부르고 또부르고....돌아가고 돌아가고 또 돌아가고...

#5!=5*4*3*2*1
#5!=5*4!
#5!=5*4*3!
#5!=5*4*3*2!
#5!=5*4*3*2*1
#팩토리얼은 1이면 끝나고 돌아가면 됨

def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)

print(factorial(10))


