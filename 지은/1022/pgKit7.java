import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        boolean[] check = new boolean[progresses.length];
        int cur = 0;
        boolean end = false;
        List<Integer> result = new ArrayList<>();
        while(!end) {
            int day = (int) Math.ceil((100.0-progresses[cur])/speeds[cur]);
            //System.out.println("현재 완료까지 걸리는 일 : "+day);
            check[cur] = true;
            int count = 1;
            for(int i=cur+1; i<progresses.length; i++) {
                //System.out.println("현재 i : "+i+", 작업진도 : "+progresses[i]+ ", 일 : "+day);
                if(!check[i] && progresses[i]+speeds[i]*day>=100) {
                    check[i]=true;
                    count++;
                } else if(progresses[i]+speeds[i]*day<100) break;
            }
            //System.out.println("count : "+count);
            result.add(count);
            boolean b = true;
            for(int i = 0; i<check.length; i++) {
                if(!check[i]) {
                    cur = i;
                    b = false;
                    break;
                }
            }
            if(b) end = true;
        }
        return result.stream().mapToInt(i->i).toArray();
    }
}