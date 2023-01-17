
import java.util.*;
import java.io.*;

public class Main {
    static int[] dx = new int[]{0, 0, -1, 1};
    static int[] dy = new int[]{-1, 1, 0, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        for (int i = 0; i < h; ++i) {

        }
        int[][] l = new int[h][w];
        boolean[][] visit = new boolean[h][w];
        for (int i = 0; i < h; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; ++j) {
                l[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ArrayDeque<Pos> q = new ArrayDeque<Pos>();
        q.add(new Pos(0, 0));
        ArrayDeque<Pos> next_q = new ArrayDeque<>();
        int time=0;
        int num =0;
        while (true) {
            while (!q.isEmpty()) {
                Pos p = q.removeFirst();
                for (int i = 0; i < 4; ++i) {
                    int next_i = dx[i] + p.i;
                    int next_j = dy[i] + p.j;
                    if (next_i >= 0 && next_i < h && next_j >= 0 && next_j < w) {
                        if (!visit[next_i][next_j]) {
                            visit[next_i][next_j] = true;
                            if (l[next_i][next_j] == 1) {
                                next_q.add(new Pos(next_i, next_j));
                            } else {
                                q.add(new Pos(next_i, next_j));
                            }
                        }
                    }
                }
            }
            if (next_q.size()!=0){
                num=next_q.size();
                q=next_q.clone();
                next_q.clear();
            }
            else{
                break;
            }
            time+=1;
        }
        System.out.println(time);
        System.out.println(num);

    }

    static public class Pos {
        int i;
        int j;

        Pos(int input_i, int input_j) {
            i = input_i;
            j = input_j;
        }
    }
}