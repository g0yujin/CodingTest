import java.io.*;
import java.util.*;

public class baekjoon2839 {
    static int N;
    static int[] arr;
    static int[]dp;
    public static void main(String[] args )throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new int[N+1];
        Arrays.fill(arr,1700);
        if(N <=5){
            arr[N] = N/3;
            if(N%3 !=0 && N%5!=0){
                arr[N] +=1;
            }
        }else{
            arr[3] =1;
            arr[4] =2;
            arr[5] =1;
            for(int i =6;i<=N; i++){
                arr[i] = Math.min(arr[i-5] +1,arr[i-3] +1);
            }
        }
        if(N ==4 ||N ==7){
            System.out.println(-1);
        }else{
            System.out.println(arr[N]);
        }
//        int basket =  0; //총 몇개의 봉지가 들어가는지
//
//        while(N>0){
//            if(N % 5  == 0){ //5로 나누어지면
//                basket += N/5;
//                break;
//            }else { //만약 아니라면 3KG이거나 봉지에 담지 나눠담지 못하는 것.
//                N -= 3;
//                basket++;
//            }
//            if(N < 0){ //차피 나눠지지 않는다면 else문에서 -3을 했기 때문에 0보다 작을 것임...
//                basket = -1;
//            }
//        }
    }
}