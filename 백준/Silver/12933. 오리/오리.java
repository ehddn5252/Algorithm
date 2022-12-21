import java.io.*;
import java.util.*;

public class Main {
    static String cry = "quack";

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        System.out.println(ans(str));
    }

    public static int ans(String str) {
        HashMap<Integer,Character> duckMap = new HashMap<>();
        int ans = 0;
        int duckNum=0;
        for (int i = 0; i < str.length(); ++i) {
            if (str.charAt(i) == cry.charAt(0)) {
                boolean flag = false;
                for(int key: duckMap.keySet()){
                    if(duckMap.get(key)==cry.charAt(4)){
                        duckMap.put(key,cry.charAt(0));
                        flag=true;
                        break;
                    }
                }
                if(!flag){
                    duckMap.put(duckNum++,cry.charAt(0));
                }
            }
            else{
                int index = cry.indexOf(String.valueOf(str.charAt(i)));
                boolean flag = false;

                for(int key: duckMap.keySet()){
                    if(duckMap.get(key)==cry.charAt(index-1)){
                        duckMap.put(key,cry.charAt(index));
                        flag=true;
                        break;
                    }
                }
                if(!flag){
                    return -1;
                }
            }
        }
        for (int key: duckMap.keySet()) {
            if (duckMap.get(key) == cry.charAt(4)) {
                ans+=1;
            }
            else{
                return -1;
            }
        }
        return ans;
    }
}