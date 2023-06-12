#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
/* DFS와 BFS
* 1. 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
* 

*/
//using namespace std;
std::vector<bool> visit;

void dfs(std::vector<std::priority_queue<int, std::vector<int>, std::greater<int>>> v,int node_num) {
	while(!v[node_num].empty()){
		int n = v[node_num].top();
		v[node_num].pop();
		if (!visit[n]) {
			visit[n] = true;
			std::cout << n << " ";
			dfs(v, n);
		}
	}
}

void bfs(std::vector<std::priority_queue<int, std::vector<int>,std::greater<int>>> v, int node_num) {
	std::queue<int> q;
	q.push(node_num);
	while (!q.empty()) {
		int popped = q.front();
		q.pop();
		while(!v[popped].empty()){
			int top = v[popped].top();
			v[popped].pop();
			if (visit[top] == false) {
				std::cout << top<<" ";
				visit[top] = true;
				q.push(top);
			}
		}
	}
}

int main() {

	int n, m, start;
	std::cin >> n >> m >> start;
	std::vector<std::priority_queue<int, std::vector<int>, std::greater<int>>> v,v1;
	
	for (int i = 0; i < n+1; ++i) {
		std::priority_queue<int, std::vector<int>, std::greater<int >> tmp;
		v.push_back(tmp);
		visit.push_back(false);
	}
	v1.resize(v.size());
	for (int i = 0; i < m; ++i) {
		int tmp1, tmp2;
		std::cin >> tmp1 >> tmp2;
		v[tmp1].push(tmp2);
		v[tmp2].push(tmp1);
	}
	std::vector<bool> visit1(visit.size());
	std::copy(visit.begin(), visit.end(), visit1.begin());
	std::copy(v.begin(), v.end(), v1.begin());

	
	visit[start] = true;
	std::cout << start << " ";
	dfs(v,start);
	std::cout << std::endl;
	visit = visit1;
	v = v1;
	visit[start] = true;
	std::cout << start << " ";
	bfs(v, start);
	std::cout << std::endl;
	return 0;
;}