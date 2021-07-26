// 모든 경우의 수를 계산하면 15Cr * 1000 적절
// 위의 경우의 수에서 겹치는 것의 개수를 찾으면 된다.
//

class Solution {
    
    static void combination(int[] arr, boolean[] visited, int start, int n, int r) {
        if(r == 0) {
            print(arr, visited, n);
            return;
        } 

        for(int i=start; i<n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }
    
    public int solution(int[][] needs, int r) {
        int answer = 0;
        return answer;
        for(int i=0;i<needs.length;++i){
            for(int j=0;j<needs[i].length;++j){
                if needs[i][j]
            }
        }
    }
}