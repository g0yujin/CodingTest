import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Set<Integer> reserveSet = Arrays.stream(reserve).boxed().collect(Collectors.toSet());
        Set<Integer> lostSet = Arrays.stream(lost).boxed().collect(Collectors.toSet());
        
        Arrays.sort(lost);
        for(int i : lost) {
            if(reserveSet.contains(i)) {
                lostSet.remove(i);
                reserveSet.remove(i);
            }
        }
        for(int i : lost) {
            if(reserveSet.contains(i-1)) {
                lostSet.remove(i);
                reserveSet.remove(i-1);
            } else if(reserveSet.contains(i+1)) {
                lostSet.remove(i);
                reserveSet.remove(i+1);
            }
        }
        return n-lostSet.size();
    }
}