import java.util.*;
import java.io.*;
import java.math.*;

public class Main {
    static final int INF = 4000001;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        int[][] arr = new int[V+1][V+1];
        for(int[] row : arr) {
            Arrays.fill(row,INF);
        }

        for(int i = 0; i<E; i++) {
            st = new StringTokenizer(br.readLine());
            arr[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
        }

        for(int a=1; a<=V; a++) {
            for(int k=1; k<=V; k++) {
                for(int b=1; b<=V; b++) {
                    arr[a][b] = Math.min(arr[a][b], arr[a][k]+arr[k][b]);
                }
            }
        }

        int result = INF;
        for(int i = 1; i<=V; i++) {
            result = Math.min(result, arr[i][i]);
        }

        if(result == INF) bw.write("-1");
        else bw.write(String.valueOf(result));

        bw.flush();
        bw.close();

    }
}