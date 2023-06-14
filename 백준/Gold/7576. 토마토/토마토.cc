#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int di[] = { 0, 0, -1, 1 };
const int dj[] = { -1, 1, 0, 0 };

int main() {
    int m, n;
    cin >> m >> n;
    vector<vector<int>> v(n, vector<int>(m));
    queue<pair<int, int>> q;
    vector<vector<bool>> visit(n, vector<bool>(m, false));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> v[i][j];
            if (v[i][j] == 1) {
                q.push({ i, j });
                visit[i][j] = true;
            }
        }
    }
    int maxTime = 0;
    while (!q.empty()) {
        int qSize = q.size();
        for (int i = 0; i < qSize; ++i) {
            int posI = q.front().first;
            int posJ = q.front().second;
            q.pop();
            for (int j = 0; j < 4; ++j) {
                int nextI = posI + di[j];
                int nextJ = posJ + dj[j];
                if (nextI < 0 || nextI >= n || nextJ < 0 || nextJ >= m) continue;
                if (v[nextI][nextJ] == -1 || visit[nextI][nextJ]) continue;
                visit[nextI][nextJ] = true;
                q.push({ nextI, nextJ });
            }
        }
        if (!q.empty()) maxTime++;
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (v[i][j] == 0 && !visit[i][j]) {
                maxTime = -1;
                break;
            }
        }
        if (maxTime == -1) break;
    }
    cout << maxTime;
    return 0;
}