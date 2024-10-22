import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int cur = 0;
        int sum = 0;
        List<Integer> result = new ArrayList<>();
        while(sum < progresses.length) {
            int day = (int) Math.ceil((100.0-progresses[cur])/speeds[cur]);
            //System.out.println("현재 완료까지 걸리는 일 : "+day);
            int count = 1;
            for(int i=cur+1; i<progresses.length; i++) {
                //System.out.println("현재 i : "+i+", 작업진도 : "+progresses[i]+ ", 일 : "+day);
                if(progresses[i]+speeds[i]*day<100) {
                    cur = i;
                    break;
                }
                count++;
            }
            //System.out.println("count : "+count);
            result.add(count);
            sum += count;
        }
        return result.stream().mapToInt(i->i).toArray();
    }
}