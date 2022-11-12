def solution(cap, n, deliveries: list, pickups):
    print(deliveries)
    print(pickups)
    ans = 0
    delivery_object_position = len(deliveries) - 1
    pickup_object_position = len(deliveries) - 1
    while delivery_object_position >= 0 or pickup_object_position >= 0:
        now_cap = cap
        can_cap = cap
        if delivery_object_position >= 0 and deliveries[delivery_object_position] != 0:
            ans += delivery_object_position + 1
            while now_cap > 0 and delivery_object_position>=0:
                if now_cap > deliveries[delivery_object_position]:
                    deliveries[delivery_object_position] = 0
                    now_cap = now_cap - deliveries[delivery_object_position]
                    delivery_object_position -= 1
                else:
                    deliveries[delivery_object_position] = deliveries[delivery_object_position] - now_cap
                    now_cap=0
            print(now_cap)
        else:
            delivery_object_position -= 1

        if pickup_object_position >= 0 and pickups[pickup_object_position] != 0:
            ans += pickup_object_position + 1
            while can_cap > 0 and pickup_object_position>=0:
                if pickups[pickup_object_position] > can_cap:
                    pickups[pickup_object_position] = pickups[pickup_object_position] - can_cap
                    can_cap=0

                else:
                    pickups[pickup_object_position] = 0
                    can_cap = can_cap - pickups[pickup_object_position]
                    pickup_object_position -= 1
            print(can_cap)
        else:
            pickup_object_position -= 1

        print("now_cap:" + str(now_cap))
        print("can_cap:" + str(can_cap))
    print(ans)
    return ans


cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
solution(cap, n, deliveries, pickups)
# result = 16
