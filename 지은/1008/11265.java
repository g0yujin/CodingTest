import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] result = new int[N+1][N+1];

        for(int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j <= N; j++) {
                result[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int k = 1; k <= N; k++) {
            for(int a = 1; a <= N; a++) {
                for(int b = 1; b <= N; b++) {
                    if(result[a][b] > result[a][k] + result[k][b]) {
                        result[a][b] = result[a][k] + result[k][b];
                    }
                }
            }
        }

        for(int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()); //출발
            int b = Integer.parseInt(st.nextToken()); //도착
            int c = Integer.parseInt(st.nextToken()); //시간

            if(result[a][b] > c) sb.append("Stay here\n");
            else sb.append("Enjoy other party\n");
        }


        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}