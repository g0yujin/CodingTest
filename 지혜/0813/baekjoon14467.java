import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon14467 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int count=0;
        int[] arr = new int[]{-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};

        //실험 for문
        for(int i = 0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            int cow = Integer.parseInt(st.nextToken());
            int location = Integer.parseInt(st.nextToken());

            if(arr[cow]==-1){
                arr[cow]=location;
            }else if(arr[cow]!= location){
                arr[cow]^=1; //^= 비트연산자 XOR : 두비트가 다를 때 1, 같을 때
                count ++;
            }
        }
        System.out.println(count);
    }
}
