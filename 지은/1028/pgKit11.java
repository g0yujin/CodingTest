import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int i : scoville) {
            pq.add(i);
        }
        
        if(pq.peek() >= K) return answer;
        
        while(true) {
            if(pq.size()<2) return -1;
            int cur = pq.poll()+pq.poll()*2;
            answer++;
            pq.add(cur);
            if(pq.peek() >= K) break;
        }
        return answer;
    }
}