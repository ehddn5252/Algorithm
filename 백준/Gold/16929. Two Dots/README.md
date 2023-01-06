# [Gold IV] Two Dots - 16929 

[문제 링크](https://www.acmicpc.net/problem/16929) 

### 성능 요약

메모리: 124408 KB, 시간: 184 ms

### 분류

깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p><a href="https://www.dots.co/twodots/">Two Dots</a>는 Playdots, Inc.에서 만든 게임이다. 게임의 기초 단계는 크기가 N×M인 게임판 위에서 진행된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6a0e30d5-c325-40e4-b8b2-e5878b8dbc49/-/preview/" style="width: 320px; height: 693px;"></p>

<p>각각의 칸은 색이 칠해진 공이 하나씩 있다. 이 게임의 핵심은 같은 색으로 이루어진 사이클을 찾는 것이다.</p>

<p>다음은 위의 게임판에서 만들 수 있는 사이클의 예시이다.</p>

<table class="table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 50%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/33712230-43d5-45f7-8b2d-dcb21b9c602c/-/preview/" style="width: 320px; height: 693px;"></td>
			<td style="width: 50%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/93730ab5-3ecf-4553-a411-50c22aa1e413/-/preview/" style="width: 320px; height: 693px;"></td>
		</tr>
	</tbody>
</table>

<p>점 k개 d<sub>1</sub>, d<sub>2</sub>, ..., d<sub>k</sub>로 이루어진 사이클의 정의는 아래와 같다.</p>

<ul>
	<li>모든 k개의 점은 서로 다르다. </li>
	<li>k는 4보다 크거나 같다.</li>
	<li>모든 점의 색은 같다.</li>
	<li>모든 1 ≤ i ≤ k-1에 대해서, d<sub>i</sub>와 d<sub>i+1</sub>은 인접하다. 또, d<sub>k</sub>와 d<sub>1</sub>도 인접해야 한다. 두 점이 인접하다는 것은 각각의 점이 들어있는 칸이 변을 공유한다는 의미이다.</li>
</ul>

<p>게임판의 상태가 주어졌을 때, 사이클이 존재하는지 아닌지 구해보자.</p>

### 입력 

 <p>첫째 줄에 게임판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 게임판의 상태가 주어진다. 게임판은 모두 점으로 가득차 있고, 게임판의 상태는 점의 색을 의미한다. 점의 색은 알파벳 대문자 한 글자이다.</p>

### 출력 

 <p>사이클이 존재하는 경우에는 "Yes", 없는 경우에는 "No"를 출력한다.</p>

