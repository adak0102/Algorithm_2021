class Node():
    def __init__(self):  #생성자 만듬
        self.data=None
        self.link=None

def printNode(current):
    print(current.data,end='-->')
    while (current.link != None):
        current=current.link
        print(current.data,end='-->')
    print()

node1=Node() #빈노드 만들어짐
node1.data='다현'

node2=Node()
node2.data='정연'   #메모리상에 어디있뜬 관계가 전혀 없음, 바로 옆에 있으나 아니나
node1.link=node2   # 둘이 연결

node3=Node()
node3.data='쯔위'
node2.link=node3
printNode(node1)

newNode=Node()
newNode.data='재남'
newNode.link=node2.link
node2.link=newNode
printNode(node1)

# print(node1.data,end='-->')
# print(node1.link.data, end='-->')
# print(node1.link.link.data,end='-->')  #어디있든 관계가 없음
# # #시작점만 알면 됨: 시작 node1 (head) 만 알면됨 : 첫노드를 아는 시작점 [pointer]
# print(node1.link.link.link.data, end='-->')

# FOR문 돌리기
# current=node1
# def print(currentNode)
# print(current.data,end='-->')
# while (current.link != None):
#     current=current.link
#     print(current.data,end='-->')

## 재남 노드를 삭제:NewNode
node2.link=node3 #link만 바꿔주면 됨 정연-->쯔위로
del (newNode)