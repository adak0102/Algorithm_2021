#원형큐: 인덱스가 3이든 0이든 front=end일떄 비어 있는것 임
#front 이전이 rear면 꽉찬 것
#원형큐는 한칸을 버릴 수 밖에 없음
#실제 데이터에서는 front=rear면 빈건지 꽉찬건지 알 수 없어서 한칸을 버림
#꽉찬거 : front이전이 rear 빈거: front=rear

##함수 선언부
def isQueueFull():
    global SIZE,queue,front,rear
    if ((rear+1)%SIZE==front):  #5로 나눈 나머지 값이  #5되면 안되니까 5넘어가지 않게 나머지 값
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE,queue,front,rear
    if (front==rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if (isQueueFull()):
        return
    #꼬리가 증가하는 것
    rear=(rear+1)%SIZE ; queue[rear]=data  #마지막꺼 5때문에 %나머지값으로

def deQeue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        return
    front=(front+1)%SIZE
    data=queue[front]
    queue[front]=None
    return data
##전역 변수부
SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=0 #-1로 주면 뒤로 가니까 선형큐랑 다르게 0으로 줌
##메인 코드부
enQueue('A');enQueue('B');enQueue('C')
print(queue)
enQueue('D')
deQeue();deQeue();deQeue();
enQueue('E');enQueue('F');
print(queue)