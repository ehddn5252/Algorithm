while True:
    A, B, C = map(int, input().split(" "))
    if A == B == C == 0:
        break

    if A == B == C:
        print("Equilateral")
    elif A + B <= C or A + C <= B or B + C <= A:
        print("Invalid")
    elif A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Scalene")
