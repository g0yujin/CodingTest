import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[] arr = new int[K];
        for(int i=0; i<K; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        long start = 1;
        long end = arr[K-1];
        long result = 0;

        while(start <= end) {
            int total = 0;
            long mid = (start + end) / 2;
            for(int i=0; i<K; i++) {
                total += arr[i]/mid;
            }

            if(total < N) end = mid - 1;
            else {
                result = mid;
                start = mid + 1;
            }
        }

        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}