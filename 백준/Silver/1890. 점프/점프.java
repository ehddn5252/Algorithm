import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Integer N = Integer.parseInt(br.readLine());
        long[][] dp = new long[N][N];
        long[][] l = new long[N][N];
        for (int i = 0; i < N; ++i) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < N; ++j) {
                l[i][j] = Long.parseLong(s[j]);
            }
        }
        dp[0][0] = 1;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                for (int k = 1; k < N; ++k) {
                    if (j - k >= 0 && l[i][j - k] == k) {
                        dp[i][j] = dp[i][j - k] + dp[i][j];
                    }
                    if (i - k >= 0 && l[i - k][j] == k) {
                        dp[i][j] = dp[i - k][j] + dp[i][j];
                    }
                }
            }
        }
        System.out.println(dp[N - 1][N - 1]);
    }
}