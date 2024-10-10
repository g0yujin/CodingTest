import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int x = Integer.parseInt(br.readLine());
        int[][] arr = new int[58][58];
        for (int i = 0; i < 58; i++) {
            for (int j = 0; j < 58; j++) {
                arr[i][j] = (int) 1e9;

                if (i == j) {
                    arr[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < x; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " => ");
            int p = convertChar(st.nextToken().charAt(0));
            int q = convertChar(st.nextToken().charAt(0));

            if (p != q) {
                arr[p][q] = 1;
            }
        }

        for (int k = 0; k < 58; k++) {
            for (int i = 0; i < 58; i++) {
                for (int j = 0; j < 58; j++) {
                    arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j]);
                }
            }
        }

        List<String> validArr = new ArrayList<>();
        for (int i = 0; i < 58; i++) {
            for (int j = 0; j < 58; j++) {
                if (arr[i][j] != (int) 1e9 && arr[i][j] != 0) {
                    char a = (char) (i + 'A');
                    char b = (char) (j + 'A');
                    validArr.add(a + " => " + b);
                }
            }
        }

        sb.append(validArr.size()).append("\n");

        for (String s : validArr) {
            sb.append(s).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int convertChar(char c) {
        if (c >= 'A' && c <= 'Z') {
            return c - 'A';
        } else {
            return c - 'a' + 32;
        }
    }

}