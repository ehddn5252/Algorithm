코딩 테스트를 위한 정리

## **list의 method**

리스트에는 다음과 같은 method들이 존재한다. 알아두자

append()

sort()

reverse()

count()

remove()

# **알아야 할 라이브러리**

## 내장 함수: sort나 sum, min, max, eval 함수가 있다.

### **eval**

```python
result = eval("(3 + 5) * 7")
```

과 같이 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.

itertools: 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다.

가장 유용하게 쓸 수 있는 클래스는 permutations, combinations이다.

permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 봅아 일렬로 나열하는 모든 경우(순열)를 계산해준다. permutations는 객체이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.

**permutation 사용 예시**

```python
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data,3))
print(result)
```

product는 permutation과 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다. 다만 원소를 중복하여 뽑는다. product 객체를 초기화할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다. product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.

**product 예시**

리스트 ['A', 'B', 'C']에서 중복을 포함하여 2개(r=2)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다.

```python
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data), repeat=2))
print(result)
```

## **combinations_with_replacement는 combinations**

와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다. 다만 원소를 중복해서 뽑는다. combinations_with_replacement는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용해야 한다.

```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)
```

## **heapq**: 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.

최소힙 구현, 오름차순 힙 정렬

```python
import heapq

def heapsort(iterable):
	h = []
	result = []

	# 모든 원소를 차례대로 힙에 삽입
	for value in iterable:
	heapq.heappush(h, value)

	# 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
	for i in range(len(h)):
		result.append(heapq.heappop(h))
	return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```

## bisect: 이진 탐색(Binary Search) 기능을 제공하는 라이브러리이다.

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a,x))
```

```python
>>> 2
>>> 4
```

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
	right_index = bisect_right(a, right_value)
	left_index = bisect_left(a, left_value)
	return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
```

```python
>>> 2
>>> 6
```

## **collections: 덱(deque), 카운터(counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리 이다.**

### **deque 사용 예시**

```python
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))
```

```python
>>> deque([1, 2, 3, 4, 5])
>>>[1, 2, 3, 4, 5]
```

### **Counter 사용 예시**

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))
```

```python
>>> 3
>>> 1
>>> {'red': 2, 'blue': 3, 'green': 1}
```

math: 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함하고 있다.

## math

```python
import math
math.factorial(5)
math.sqrt(7)
math.gcd(21,14)
math.pi
math.e
```
