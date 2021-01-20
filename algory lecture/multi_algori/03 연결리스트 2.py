##함수 선언부
class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNode(current):
    print(current.data,end='-->')
    while (current.link != None):
        current=current.link
        print(current.data,end='-->')
    print()

def insert_node(findData,insertData):
    global head,pre,cur
    #입력할 데이터가 제일 처음이 될때...
    if head.data==findData:
        node=Node()
        node.data=insertData
        node.link=head
        head=node ##??
        return
    #입력데이터가 중간에 있을때..
    current=head  #??
    #몇개인지 모를때는 while 무한루프 돌리는게 맞음, 조건에만 맞으면 빠져나오게
    while current.link!=None:  #currentlink=None이면 끝번호 / 원형연결리스트에서는 currentLink가 head임
        pre=current
        current=current.link
        if current.data==findData:
            node=Node()
            node.data=insertData
            node.link=current
            pre.link=node
            memory.append(node)  #memory.append(node): 파이썬은 append하면 끝나는데 #이거는 프로그래밍 언어차원, 자료구조 (C언어)
            return

    #findData를 못찾음
    node=Node();node.data=insertData
    current.link=node


##전역 변수부
memory=[]
head,cur,pre=None,None,None #시작노드,현재노드,앞노드
dataAry=['다현','정연','쯔위']

##메인 코드부
# if __name__=='__main__':   #진입점, 어디서부터 읽을지 #여기서 부터 읽겠다는 거?!
#     pass
if __name__=='__main__':
    node=Node()
    node.data=dataAry[0]
    head=node
    memory.append(node)
    for data in dataAry[1:]:
        pre=node
        node=Node()
        node.data=data
        pre.link=node
        memory.append(node)

    printNode(head)
    insert_node('다현','화사')
    printNode(head)
    insert_node('쯔위','재남')
    printNode(head)
    insert_node('없다','막내')