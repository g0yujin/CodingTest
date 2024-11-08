import java.math.*;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        BigInteger[][] d = new BigInteger[N+1][N+1];

        //배열 초기화 해줘야함!!!
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= N; j++) {
                d[i][j] = BigInteger.ZERO;
            }
        }

        for(int i = 1; i <= N; i++) {
            d[i][i] = BigInteger.valueOf(1);
            d[i][0] = BigInteger.valueOf(1);
            d[i][1] = BigInteger.valueOf(i);
        }

        for(int i = 2; i <= N; i++) {
            for(int j = 1; j <=i; j++) {
                d[i][j] = d[i-1][j-1].add(d[i-1][j]);

            }
        }

        bw.write(String.valueOf(d[N][M]));
        bw.flush();
        bw.close();
    }
}