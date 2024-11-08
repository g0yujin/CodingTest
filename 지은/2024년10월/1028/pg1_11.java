import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> aList = new ArrayList<>();
        for(int a : arr) {
            if(a % divisor == 0) {
                aList.add(a);
            }
        }
        
        if(aList.size() == 0) aList.add(-1);
        Collections.sort(aList);
        return aList.stream().mapToInt(i->i).toArray();
    }
}