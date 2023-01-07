n, w, L = map(int, input().split(" "))  # 트럭수 다리 길이, 다리 하중
l = list(map(int, input().split(" ")))

from collections import deque

trucks = deque(l)

bridge = deque([0 for i in range(w)])
bridge_w = 0
time = 0
while trucks:
    truck = trucks.popleft()
    bridge_w -= bridge.popleft()
    while L < bridge_w + truck:
        time += 1
        bridge.append(0)
        bridge_w -= bridge.popleft()
    bridge_w += truck
    bridge.append(truck)
    time += 1
print(time+w)
