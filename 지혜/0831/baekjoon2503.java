
import java.util.*;
import java.io.*;

public class baekjoon2503{
    static int N;
    static boolean[] check = new boolean[1000];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for(int i =123; i<1000; i++){
            String str = Integer.toString(i);
            if(str.charAt(0) =='0' || str.charAt(1)=='0' || str.charAt(2)=='0') continue;
            if(str.charAt(0)==str.charAt(1) || str.charAt(0)==str.charAt(2) || str.charAt(1)==str.charAt(2)) continue;
            check[i] = true;
        }
        N = Integer.parseInt(br.readLine());
        for(int i =0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            int req = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            //예상 가능한 모든 정답 탐색
            for(int ans =123; ans<1000; ans++){
                if(check[ans]){
                    int ns =0;
                    int nb =0;

                    for(int j=0; j<3; j++){
                        char req_split = Integer.toString(req).charAt(j);
                        for(int k=0; k<3;k++){
                            char ans_split = Integer.toString(ans).charAt(k);

                            //스트라이크 볼 계산
                            if(req_split==ans_split && j == k){
                                ns++;
                            }else if(req_split == ans_split && j != k){
                                nb++;
                            }
                        }
                    }
                    if(ns ==s &&nb==b){
                        check[ans] =true;
                    }
                    else {
                        check[ans] =false;
                    }
                }
            }
        }
        int ans =0;
        for(int i =123; i<1000; i++){
            if(check[i]) ans++;
        }
        System.out.println(ans);
    }
}