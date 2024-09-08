import java.util.*;
import java.io.*;

public class baekjoon14916{
    static int n,result;
    static int[] mondey ={5,2};
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        while(true){
            if(n%5==0){
                result += n/5;
                System.out.println(result);
                break;
            }else{
                n-=2;
                result++;
            }
            if(n<0){
                System.out.println(-1);
                return;
            }
        }
    }
}