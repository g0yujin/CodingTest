import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int[] d = new int[n + 1];
		
		d[0] = 0;
		d[1] = 1;
		for(int i = 2; i <= n; i++) {
			d[i] = d[i - 1];
			for(int j = 1; j*j <= i; j++) {
				d[i] = Math.min(d[i], d[i - (j*j)]);
			}
			d[i]++;
		}
		bw.write(String.valueOf(d[n]));
        bw.flush();
        bw.close();
	}

}