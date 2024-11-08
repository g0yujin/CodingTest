import java.util.*;

class Solution {
    Set<Integer> set = new HashSet<>();
    public int solution(String numbers) {
        recursive("", numbers);
        return set.size();
    }
    
    void recursive(String s, String o) {
        if(!s.equals("")) {
            int res = Integer.parseInt(s);
            if(isPrime(res)) set.add(res);
        }
        
        for(int i=0; i<o.length(); i++) {
            recursive(s+o.charAt(i), o.substring(0,i)+o.substring(i+1));
        }
    }
    
    boolean isPrime(int num) {
        if(num == 0 || num == 1) return false;
        for(int i=2; i<=Math.sqrt(num); i++) {
            if(num%i == 0) return false;
        }
        return true;
    }
}