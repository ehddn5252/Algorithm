# 작성자 : 김동우
# 작성일자 : 2021.09.25
# 문제명 : DFS와 BFS


class DFS:

    def __init__(self,vertex_num:int=1, start_node:int=1,edge_list:list=[]) -> None:
        if not isinstance(start_node,int):
            start_node=int(start_node)

        self.start_node: int = start_node
        self.stack:list=[self.start_node]
        self._visit_list:list=[self.start_node]
        self._edge_list:list = edge_list
        # 0번째 인덱스 무시하기 위해 vetex_num + 1 로 둔다
        self.vertex_maxtirx:list=[[]for _ in range(vertex_num+1)]

    def set_vertex_maxtirx(self):
        for i,(v1,v2) in enumerate(self.edge_list):
            self.vertex_maxtirx[v1].append(v2)
            self.vertex_maxtirx[v2].append(v1)
        
        for i in range(len(self.vertex_maxtirx)):
            self.vertex_maxtirx[i].sort(reverse=True)

    @property
    def edge_list(self):
        return self._edge_list

    @edge_list.setter
    def edge_list(self,value):
        self._edge_list = value

    def is_empty(self):
        ret = False
        if not self.stack:
            ret= True
        return ret

    def top(self):
        print(self.stack[-1])

    def pop(self):
        return self.stack.pop(-1)

    def find_around_vertex_and_append_stack(self,popped_vertex:str):
        """
        input list`s form example: [(vertex1, vertex2), (vertex1, vertex3), (vertex4, vertex2)]
        """
        if not isinstance(popped_vertex,str):
            popped_vertex = str(popped_vertex)

        for _,(vertex1,vertex2) in enumerate(self.edge_list):
            if popped_vertex == vertex1:
                if vertex2 not in self._visit_list:
                    self._visit_list.append(vertex2)
                    self.stack.append(vertex2)

            elif popped_vertex == vertex2:
                if vertex1 not in self._visit_list:
                    self._visit_list.append(vertex1)
                    self.stack.append(vertex1)
            
    def find_around_vertex_and_append_stack2(self,popped_vertex:int):
        """
        input list`s form example: [(vertex1, vertex2), (vertex1, vertex3), (vertex4, vertex2)]
        """
        if not isinstance(popped_vertex,int):
            popped_vertex = int(popped_vertex)

        for check_vertex in (self.vertex_maxtirx[popped_vertex]):
            if check_vertex not in self._visit_list:
                self._visit_list.append(check_vertex)
                self.stack.append(check_vertex)


class BFS:
    def __init__(self) -> None:
        self.queue = []
    
    def pop(self):
        return self.queue.pop(0)

    def top(self):
        print(self.queue[0])



# 이제 line_degree에 간선정보 다 넣어놓았다. DFS 와 BFS를 구현하자.
# DFS는 깊이 우선 탐색으로 시작점을 기준으로 연결된 노드를 stack에 넣고 pop하고 연결하고 넣고 반복하는 작업
'''
기본작업
0. 시작 노드를 stack에 넣는다.

1. stack pop한다.
2. pop한 노드와 연결된 노드를 모두 stack에 넣는다.
3. while(stack): repeat try 1, try 2
'''

# 입력

if __name__=="__main__":
    # 정점의 개수, 간선의 개수, 시작 정점의 번호
    N,M,V = map(int,input().split())
    edge_list:list= []
    for i in range(M):
        line = tuple(map(int,input().split()))
        edge_list.append(line)

    # dfs부터
    dfs1 = DFS(vertex_num = N, start_node = V, edge_list = edge_list)
    print(dfs1.edge_list)
    #dfs1.edge_list = edge_list
    dfs_answer:list = []
    dfs1.set_vertex_maxtirx()
    while dfs1.stack:
        popped_vertex = dfs1.pop()
        dfs_answer.append(popped_vertex)
        dfs1.find_around_vertex_and_append_stack2(popped_vertex=popped_vertex)
    print(dfs_answer)
        
