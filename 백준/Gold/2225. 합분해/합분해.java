
import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        long[][] dp = new long[K + 1][N + 1];
        for (int j = 0; j <= N; ++j) {
            dp[1][j] = 1;
        }
        for (int i = 1; i < K + 1; ++i) {
            for (int j = 0; j < N + 1; ++j) {
                for (int k = 0; k < j + 1; ++k) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k])%1000000000;
                }
            }
        }
        System.out.println(dp[K][N]);
    }
}