import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int result = 0;

        while(n>0) {
            if(n%5 == 0) {
                result += n/5;
                n = 0;
            } else {
                result += 1;
                n -= 3;
            }
        }
        if(n != 0) {
            result = -1;
        }


        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();

    }

}