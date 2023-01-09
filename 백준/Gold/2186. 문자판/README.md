# [Gold III] 문자판 - 2186 

[문제 링크](https://www.acmicpc.net/problem/2186) 

### 성능 요약

메모리: 127688 KB, 시간: 1196 ms

### 분류

다이나믹 프로그래밍(dp), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>알파벳 대문자가 한 칸에 한 개씩 적혀있는 N×M 크기의 문자판이 있다. 편의상 모든 문자는 대문자라 생각하자. 예를 들어 아래와 같은 문자판을 보자.</p>

<table class="table table-bordered" style="width: 16%;">
	<tbody>
		<tr>
			<td style="width: 4%; text-align: center;">K</td>
			<td style="width: 4%; text-align: center;">A</td>
			<td style="width: 4%; text-align: center;">K</td>
			<td style="width: 4%; text-align: center;">T</td>
		</tr>
		<tr>
			<td style="width: 4%; text-align: center;">X</td>
			<td style="width: 4%; text-align: center;">E</td>
			<td style="width: 4%; text-align: center;">A</td>
			<td style="width: 4%; text-align: center;">S</td>
		</tr>
		<tr>
			<td style="width: 4%; text-align: center;">Y</td>
			<td style="width: 4%; text-align: center;">R</td>
			<td style="width: 4%; text-align: center;">W</td>
			<td style="width: 4%; text-align: center;">U</td>
		</tr>
		<tr>
			<td style="width: 4%; text-align: center;">Z</td>
			<td style="width: 4%; text-align: center;">B</td>
			<td style="width: 4%; text-align: center;">Q</td>
			<td style="width: 4%; text-align: center;">P</td>
		</tr>
	</tbody>
</table>

<p>이 문자판의 한 칸(아무 칸이나 상관없음)에서 시작하여 움직이면서, 그 칸에 적혀 있는 문자들을 차례대로 모으면 하나의 단어를 만들 수 있다. 움직일 때는 상하좌우로 K개의 칸까지만 이동할 수 있다. 예를 들어 K=2일 때 아래의 그림의 가운데에서는 'X' 표시된 곳으로 이동할 수 있다.</p>

<table class="table table-bordered" style="width: 20%;">
	<tbody>
		<tr>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;">X</td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;"> </td>
		</tr>
		<tr>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;">X</td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;"> </td>
		</tr>
		<tr>
			<td style="width: 4%; text-align: center;">X</td>
			<td style="width: 4%; text-align: center;">X</td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;">X</td>
			<td style="width: 4%; text-align: center;">X</td>
		</tr>
		<tr>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;">X</td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;"> </td>
		</tr>
		<tr>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;">X</td>
			<td style="width: 4%; text-align: center;"> </td>
			<td style="width: 4%; text-align: center;"> </td>
		</tr>
	</tbody>
</table>

<p>반드시 한 칸 이상 이동을 해야 하고, 같은 자리에 머물러 있을 수 없다. 또, 같은 칸을 여러 번 방문할 수 있다.</p>

<p>이와 같은 문자판과 K, 그리고 하나의 영단어가 주어졌을 때, 이와 같은 영단어를 만들 수 있는 경로가 총 몇 개 존재하는지 알아내는 프로그램을 작성하시오.</p>

<p>위의 예에서 영단어가 BREAK인 경우에는 다음과 같이 3개의 경로가 존재한다. 앞의 수는 행 번호, 뒤의 수는 열 번호를 나타낸다.</p>

<ul>
	<li>(4, 2) (3, 2) (2, 2) (1, 2) (1, 1)</li>
	<li>(4, 2) (3, 2) (2, 2) (1, 2) (1, 3)</li>
	<li>(4, 2) (3, 2) (2, 2) (2, 3) (1, 3)</li>
</ul>

### 입력 

 <p>첫째 줄에 N(1 ≤ N ≤ 100), M(1 ≤ M ≤ 100), K(1 ≤ K ≤ 5)가 주어진다. 다음 N개의 줄에는 M개의 알파벳 대문자가 주어지는데, 이는 N×M 크기의 문자판을 나타낸다. 다음 줄에는 1자 이상 80자 이하의 영단어가 주어진다. 모든 문자들은 알파벳 대문자이며, 공백 없이 주어진다.</p>

### 출력 

 <p>첫째 줄에 경로의 개수를 출력한다. 이 값은 2<sup>31</sup>-1보다 작거나 같다.</p>

