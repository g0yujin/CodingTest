import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Deque<Node> queue = new ArrayDeque<>();
        for(int i=0; i<priorities.length; i++) {
            queue.add(new Node(i, priorities[i]));
        }
        
        Arrays.sort(priorities);
        while(!queue.isEmpty()) {
            Node cur = queue.removeFirst();
            if(cur.p == priorities[priorities.length-answer-1]) {
                answer++;
                if(cur.x == location) break;
            }
            else queue.add(cur);
            
        }
        return answer;
    }
}

class Node {
    int x;
    int p;
    
    public Node(int x, int p) {
        this.x = x;
        this.p = p;
    }
}