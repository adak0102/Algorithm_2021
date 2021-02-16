#############################패캠#########################################
#bfs패캠_list 이용
graph=dict()
graph['A']=['B','C']
graph['B']=['','']
graph['C']=['','']
graph['D']=['','']



#need_visit 큐와, visited 큐 두개의 큐 생성

def bfs(graph, start_node):
    visited=list()
    need_visit=list()

    need_visit.append(start_node)

    while need_visit:
        node=need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph(node)) #뒤에 붙이기

        return  visited


bfs(graph,'A')

#bfs 시간복잡도
# 노드수 :V 간선수 :E
# 시간복잡도 : O(V+E)


#dfs 알고리즘 구현
#need_visit 스택방식,
def dfs(graph, start_node):
    visited, need_visit=list(),list()

    while need_visit:
        node=need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph(node))
    return visited
