import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] d = new int[N+1];
        int[] arr = new int[N+1];
        for(int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        d[1] = arr[1];
        if(N > 1)  {
            d[2] = arr[1] + arr[2];

            for(int i=3; i<=N; i++) {
                d[i] = Math.max(d[i-3] + arr[i-1], d[i-2]) + arr[i];
            }
        }

        bw.write(String.valueOf(d[N]));
        bw.flush();
        bw.close();
    }
}