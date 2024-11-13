import java.util.*;

class Solution {
    boolean[] visit;
    int max = Integer.MIN_VALUE;
    public int solution(int k, int[][] dungeons) {
        visit = new boolean[dungeons.length];
        dfs(0, dungeons, k);
        return max;
    }
    
    void dfs(int n, int[][] dungeons, int k) {
        for(int i=0; i<dungeons.length; i++) {
            if(!visit[i] && dungeons[i][0] <= k) {
                visit[i] = true;
                dfs(n+1, dungeons, k-dungeons[i][1]);
                visit[i] = false;
            }
        }
        System.out.println(n);
        max = Math.max(max, n);
    }
}