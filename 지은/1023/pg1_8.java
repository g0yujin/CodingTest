import java.util.*;

class Solution {
    public long solution(long n) {
        String s = String.valueOf(n);
        char[] arr = new char[s.length()];

        for(int i=0; i<s.length(); i++) {
            arr[i] = s.charAt(i);
        }

        Arrays.sort(arr);

        StringBuilder res = new StringBuilder();
        for(int i = arr.length-1; i>=0; i--) {
            res.append(arr[i]);
        }
        
        return Long.parseLong(res.toString());
    }
}