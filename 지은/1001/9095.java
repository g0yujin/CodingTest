import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        int[] d = new int[12];

        d[1] = 1;
        d[2] = 2;
        d[3] = 4;
        for(int i=4; i<=11; i++) {
            d[i] = d[i-3]+d[i-2]+d[i-1];
        }

        for(int t=0; t<T; t++) {
            int n = Integer.parseInt(br.readLine());
            sb.append(d[n]).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}