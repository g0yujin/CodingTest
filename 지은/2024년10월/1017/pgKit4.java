import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 0;
        
        Map<String, Integer> map = new HashMap<>();
        for(int i = 0; i<clothes.length; i++) {
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1],0)+1);
        }
        
        int answer2 = 1;
        for(int i : map.values()) {
            answer += i;
            answer2 *= i+1;
        }
        
        return map.keySet().size() == 1 ? answer : answer2-1;
    }
}