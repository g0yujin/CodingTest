import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] d = new int[N+1];

        for(int i=2; i<=N; i++){
            int cur = Integer.MAX_VALUE;
            if(i % 3 == 0) cur = Math.min(cur, d[i/3] + 1);
            if(i % 2 == 0) cur = Math.min(cur,d[i/2] + 1);
            cur = Math.min(cur,d[i-1]+1);
            d[i] = cur;
        }

        bw.write(String.valueOf(d[N]));
        bw.flush();
        bw.close();
    }
}