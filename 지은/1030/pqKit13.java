import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        PriorityQueue<Integer> revPq = new PriorityQueue<>(Collections.reverseOrder());
        for(String s : operations) {
            char c = s.charAt(0);
            if(c == 'I') {
                int a = Integer.parseInt(s.substring(2));
                pq.add(a);
                revPq.add(a);
            } else {
                if(s.equals("D -1") && !pq.isEmpty()) {
                    int re = pq.remove();
                    revPq.remove(re);
                } else if(s.equals("D 1") && !revPq.isEmpty()) {
                    int re = revPq.remove();
                    pq.remove(re);
                }
            }
        }

        return pq.isEmpty() ? new int[]{0,0} : new int[]{revPq.remove(),pq.remove()};
        
    }
}