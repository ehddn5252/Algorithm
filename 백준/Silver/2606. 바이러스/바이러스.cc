#include<iostream>
#include<vector>
/*
2606 virus

1. 첫째 줄에는 컴퓨터의 수가 주어진다. 
2. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
3. 이어서 한 쌍씩 네트워크 상에서 직접 여결되어 있는 컴퓨터의 번호 쌍이 주어진다.

해결 방법:

1. 백터에 넣는다.

*/


using namespace std;

#include<queue>
#include<algorithm>



vector<bool> visit;

void dfs(vector<vector<int>> v_2d,int start) {
    for (auto i = 0; i < v_2d[start].size(); ++i) {
        if (visit[v_2d[start][i]] == false) {
            visit[v_2d[start][i]] = true;
            dfs(v_2d, v_2d[start][i]);
        }
    }
}


int main() {
    int n,m;
    cin >> n>> m;
    
    vector<vector<int>> v_2d;
    const int const_n = n;


    for (int i = 0; i < n+1; ++i) {
        vector<int> v_tmp;
        v_2d.push_back(v_tmp);
        visit.push_back(false);
    }
    visit[1] = true;
    
    for (auto i = 0; i < m; ++i) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        v_2d[tmp1].push_back(tmp2);
        v_2d[tmp2].push_back(tmp1);
    }
    dfs(v_2d, 1);
    int ans = 0;
    for (int i = 0; i < visit.size(); ++i) {
        if (visit[i] == true) {
            ans += 1;
        }
    }
    cout << ans-1;

    return 0;
}