import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        long[] arr = new long[N];
        for(int i=0; i<N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);

        long min = 0;
        long max = arr[N-1];
        long result = 0;

        while(min <= max) {
            long mid = (min + max) / 2;
            long cur = 0;
            for(int i=0; i<N; i++) {
                long cut = arr[i]-mid;
                if(cut>0) {
                    cur += cut;
                }
            }

            if(cur < M) {
                max = mid-1;
            }
            else  {
                min = mid+1;
                result = mid; //반복문이 진행될수록 총 길이가 M이거나 가까워지므로 정답을 기록.
            }

        }

        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}