import java.util.*;
import java.io.*;

public class baekjoon11727{
    static int n;
    static int[]dp;
    static int cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        dp = new int[n+1];
        simulation();
        System.out.println(dp[n]);
    }
    public static void simulation(){
        dp[1]= 1;
        dp[2] =3;

            for(int i =3; i<n+1; i++){
                dp[i] = (2*dp[i-2]+dp[i-1])%10007;

        }
    }
}