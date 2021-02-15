# 작성일자 : 20210208
# 문제명 : [프로그래머스 힙] 이중 우선순위 큐
# 문제 요약 : 

def solution(operations):
    queue=[]
    try: 
        for operation in operations:
            # 만약 I로 시작하면 queue에 넣는다
            if operation[0]=="I":
                queue.append(int(operation[2:])) 
            # queue에 아무것도 없는데 pop하려 하면 그냥 지나친다.
            elif not queue and operation[0]=="D":
                continue
            # 최대 값을 pop한다
            elif operation=="D 1":
                queue.remove(max(queue))
            # 최소 값을 pop한다
            elif operation=="D -1":
                queue.remove(min(queue))
        # 큐가 비어있으면 [0,0]을 pop
        if not queue:
            return [0,0]
            #print(f"[0],[0]")
        # 아니면 [max,min]을 pop한다.
        else:
            return [max(queue),min(queue)]
            #print(f"[{max(queue)},{min(queue)}]")
    except:
        return [0,0]
        print(f"[0],[0]")

if __name__=="__main__":
    operations1=["I 16","D 1"]
    operations=["I 7","I 5","I -5","D -1"]
    solution(operations1)