import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        for(int i=0; i<citations.length; i++) {
            int max = citations.length-i;
            if(citations[i]>=max) {
                return max;
            }
        }
        return 0;
    }
}