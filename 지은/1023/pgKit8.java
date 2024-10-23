import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<String> stack = new ArrayDeque<>();

        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == ')') {
                if(stack.isEmpty()) return false;
                String c = stack.pop();
                if(c.equals(String.valueOf(s.charAt(i))))  return false;
            }
            else stack.push(String.valueOf(s.charAt(i)));
        }

        return stack.isEmpty();
    }
}