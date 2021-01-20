queue=[None for _ in range(3)]
front=rear=-1

rear+=1;queue[rear]='A'
rear+=1;queue[rear]='B'
rear+=1;queue[rear]='C'
print(queue)
front+=1;print(queue[front]);queue[front]=None #안해되 되는데 확실히 하려고
front+=1;print(queue[front]);queue[front]=None
front+=1;print(queue[front]);queue[front]=None
print(queue)
rear+=1;queue[rear]='D' #이런 한계 때문에 원형큐 사용

