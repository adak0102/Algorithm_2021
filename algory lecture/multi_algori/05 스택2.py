#함수 선언부
#isStackEmpty(),pop()
def isStackEmpty():
    if top==None:
        return True
    else:
        return False
def pop():
    global stack,top
    if(isStackEmpty()):
        print('스택 빔!')
        return
    print("뽑기-->",stack[top])
    stack[top]=None
    top-=1

def isStackFull():
    if (top==SIZE-1):
        return True
    else:
        return False

def push(data):
    global stack,top
    if(isStackFull()):  #스택 꽉차있는지 확인하고 넣음
        print('스택 꽉참!')
        return
    top+=1
    stack[top]=data

#전역 변수부
SIZE=5  #운영체제마다 정해져 있는 것임
stack=[None for _ in range(SIZE)]
top=-1
#메인 코드부