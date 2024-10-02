import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        long[] d = new long[N+1];
        d[1] = 1;
        d[2] = 2;

        for(int i=3; i<=N; i++) {
            d[i] = (d[i-2] + d[i-1])%10007;
        }

        bw.write(String.valueOf(d[N]));
        bw.flush();
        bw.close();
    }
}