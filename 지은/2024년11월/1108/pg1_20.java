import java.util.*;

class Solution {
    public String solution(int n) {
        String[] sArr = {"수","박"};
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<n; i++) {
            sb.append(sArr[i % 2]);
        }
        return sb.toString();
    }
}