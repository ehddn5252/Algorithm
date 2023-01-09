
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] map, mapCopyyed, d={{1,0},{-1,0},{0,1},{0,-1}};
    static boolean[][] visit;
    static boolean[] combiVisit;
    static int ans,zeroCount, N,M;
    static ArrayList<Pos> l,lCopy,qCloned;
    static Queue<Pos> q;
    static int countCombinationNum;
    public static void main(String[] args) throws IOException {
        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);
        map = new int[N][M];
        mapCopyyed = new int[N][M];
        visit = new boolean[N][M];
        l=new ArrayList<Pos>(){};
        lCopy=new ArrayList<Pos>();
        q = new LinkedList<Pos>();
        qCloned = new ArrayList<Pos>();
        for(int i=0;i<3;++i){
            l.add(new Pos(0,0));
        }

        for(int i=0;i<N;++i){
            s = br.readLine().split(" ");
            for(int j=0;j<M;++j){
                map[i][j] = Integer.parseInt(s[j]);
                mapCopyyed[i][j]=map[i][j];
                if(map[i][j]==0){
                    lCopy.add(new Pos(i,j));
                }
                else if(map[i][j]==2){
                    q.offer(new Pos(i,j));
                    qCloned.add(new Pos(i,j));
                }
            }
        }
        combiVisit=new boolean[lCopy.size()];
        combination(0,3);
        System.out.println(ans);
//        System.out.println(countCombinationNum);
    }


    private static void combination(int cnt,int r) {
        /*
        1은 벽
        2는 바이러스
        0은 공간이다.
        벽은 3개 칠 수 있고, 벽을 치는 경우
         */
        if(cnt==r){
//            countCombinationNum++;
            virusBFS();
            int count=countAns();
            if(count>ans){
                ans=count;
            }
            resetMap();
            resetQ();
            resetVisit();
            return;
        }

        for(int i=cnt;i< lCopy.size();++i){
            if(combiVisit[i])continue;
            combiVisit[i]=true;
            l.set(cnt,lCopy.get(i));
            combination(cnt+1,r);
            combiVisit[i]=false;
        }
    }

    private static void virusBFS() {
        for(int i=0;i<3;++i){
            Pos p = l.get(i);
            map[p.i][p.j]=1;
        }
        while(!q.isEmpty()){
            Pos polled = q.poll();
            visit[polled.i][polled.j] = true;
            for(int i=0;i<4;++i){
                int nextI = polled.i+d[i][0];
                int nextJ = polled.j+d[i][1];

                if(nextI>=0 && nextI<N && nextJ>=0 && nextJ<M && map[nextI][nextJ]==0){
                    if (visit[nextI][nextJ]) continue;
                    map[nextI][nextJ]=2;
                    q.offer(new Pos(nextI,nextJ));
                }
            }
        }
    }

    private static int countAns(){
        int count=0;
        for(int i=0;i<N;++i){
            for(int j=0;j<M;++j){
                if(map[i][j]==0){
                    count+=1;
                }
            }
        }
        return count;
    }

    private static void resetQ(){
        for(int i=0;i< qCloned.size();++i){
            q.offer(qCloned.get(i));
        }
    }
    private static void resetMap(){
        for(int i=0;i<N;++i){
            for(int j=0;j<M;++j){
                map[i][j] = mapCopyyed[i][j];
            }
        }
    }
    private static void resetVisit(){
        for(int i=0;i<N;++i){
            for(int j=0;j<M;++j){
                visit[i][j] = false;
            }
        }
    }

    static class Pos{
        int i;
        int j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }

        @Override
        public String toString() {
            return "Pos{" +
                    "i=" + i +
                    ", j=" + j +
                    '}';
        }
    }
}
