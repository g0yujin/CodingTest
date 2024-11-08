import java.util.*;
import java.io.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        int[] d = new int[N];
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i =0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            d[i] = 1;
        }

        int max = Integer.MIN_VALUE;
        for(int i=0; i<N; i++) {
            for(int j=0; j<i; j++) {
                if(arr[i]>arr[j]) d[i] = Math.max(d[i],d[j]+1);
            }
            max = Math.max(d[i],max);
        }

        bw.write(String.valueOf(max));
        bw.flush();
        bw.close();
    }
}