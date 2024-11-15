import java.util.*;

class Solution {
    int[] parent;
    public int solution(int n, int[][] wires) {
        int min = Integer.MAX_VALUE;
        
        for(int i=0; i<n-1; i++) {
            parent = new int[n+1];
            for(int j=0; j<parent.length; j++) {
                parent[j] = j;
            }
            for(int j=0; j<n-1; j++) {
                if(i==j) continue;
                union(wires[j][0], wires[j][1]);
            }
            min = Math.min(min, checkGap());
        }
        return min;
    }
    
    int find(int a) {
        if(a == parent[a]) return a;
        return parent[a] = find(parent[a]);
    }
    
    void union(int a, int b) {
        a = find(a);
        b = find(b);
        if(a>b) parent[a] = b;
        else parent[b] = a;
    }
    
    int checkGap() {
        int count1 = 1;
        int count2 = 0;
        int count1Value = find(parent[1]);
        for(int i=2; i<parent.length; i++) {
            if(find(parent[i]) == count1Value) count1++;
            else count2++;
        }
        return Math.abs(count1-count2);
    }
}