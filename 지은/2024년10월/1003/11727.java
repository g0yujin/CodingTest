import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] d = new int[N+1];

        d[1] = 1;

        if(N > 1) {
            for(int i = 2; i <= N; i++) {
                if(i % 2 == 0) d[i] = (d[i-1]*2+1)%10007;
                else d[i] = (d[i-1]*2-1)%10007;
            }
        }

        bw.write(String.valueOf(d[N]));
        bw.flush();
        bw.close();
    }
}