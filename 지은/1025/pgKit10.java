import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Integer> q = new ArrayDeque<>();
        int cur = 1;
        int sec = 1;
        int curTruckWeight = truck_weights[0];
        q.add(curTruckWeight);
        while(!q.isEmpty()) {
            if(cur == truck_weights.length) {
                sec += bridge_length;
                break;
            }
            
            if(q.size()+1 > bridge_length) {
                curTruckWeight -= q.removeFirst();
            } 
            int curTruck = truck_weights[cur];
            if(curTruckWeight+curTruck>weight) {
                q.add(0);
            } else {
                q.add(curTruck);
                curTruckWeight += curTruck;
                cur++;
            }
            sec++;
        }
        return sec;
    }
}