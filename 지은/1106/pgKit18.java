import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int maxMax = 0;
        int minMax = 0;
        for(int[] size : sizes) {
            maxMax = Math.max(maxMax, Math.max(size[0], size[1]));
            minMax = Math.max(minMax, Math.min(size[0], size[1]));
        }
        return minMax*maxMax;
    }
}