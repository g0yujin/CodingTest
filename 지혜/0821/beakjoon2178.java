import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class beakjoon2178 {
    static int n,m;
    static int[][] map;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static boolean[][] visit;
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visit = new boolean[n][m];
        for (int i =0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j<m; j++){
                map[i][j] =Integer.parseInt(st.nextToken());
            }
        }
        bfs(0,0);


    }
    public static void bfs(int x, int y){

    }
}
