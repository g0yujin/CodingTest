import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        long M = Long.parseLong(st.nextToken());

        long[] t = new long[N];
        for(int i=0; i<N; i++) {
            t[i] = Long.parseLong(br.readLine());
        }

        Arrays.sort(t);
        long start = 1;
        long end = t[N - 1] *M;

        while(start <= end) {
            long mid = (end+start) / 2;
            long count = 0;
            for(int i=0; i<N; i++) {
                count += mid/t[i]; //각 시간으로 나눈 값을 더한다(심사 받은 사람 수)

                if(count >= M) break; //오버플로우가 발생할 수도 있어서 break 해줘야함
            }

            if(count < M)
                start = mid + 1;
            else
                end = mid - 1;

        }


        bw.write(String.valueOf(start));
        bw.flush();
        bw.close();
    }
}