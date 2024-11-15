import java.util.*;

class Solution {
    Map<String,Integer> str = new HashMap<>();
    int index = 1;
    char[] cList = {'A', 'E', 'I', 'O', 'U'};
    public int solution(String word) {
        dfs("",0);
        return str.get(word);
    }
    
    void dfs(String s, int n) {
        if(n>5) return;
        if(!s.equals("")) {
            str.put(s, index);
            index += 1;
        }
        for(int i=0; i<5; i++) {
            dfs(s+cList[i], n+1);
        }
    }
}