import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] arr = new long[N];
        for(int i=0; i<N; i++) {
            arr[i]=Long.parseLong(st.nextToken());
        }

        long[] d = new long[N];
        Arrays.fill(d,Long.MAX_VALUE);

        d[0] = 0;
        for(int i=1; i<N; i++) {
            for(int j=0; j<i; j++) {
                long max = Math.max((i - j) *(1+Math.abs(arr[j]-arr[i])),d[j]); //이전까지의 k값과 비교하여 더 큰 값을 저장
                d[i] = Math.min(max,d[i]); //i까지 가는 경우의 수 중 최소값 저장
            }
        }


        bw.write(String.valueOf(d[N-1]));
        bw.flush();
        bw.close();
    }
}