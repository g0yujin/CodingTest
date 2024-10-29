import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        Arrays.sort(jobs,(a,b)->a[0]-b[0]);
        PriorityQueue<Job> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.time));
        pq.add(new Job(jobs[0][0],jobs[0][1]));

        int result = jobs[0][0];
        int index = 1;
        int end = jobs[0][1];
        while(!pq.isEmpty()){
            Job cur = pq.remove();
            for(int i = index;i<jobs.length;i++){
                if(jobs[i][0]>end+cur.time) break;
                pq.add(new Job(jobs[i][0],jobs[i][1]));
                index++;
            }

            if(index < jobs.length){
                pq.add(new Job(jobs[index][0],jobs[index][1]));
                index++;
            }

            result += (result-cur.start)+cur.time;
        }


        return result/jobs.length;
    }
}

class Job{
    int start;
    int time;

    public Job(int start, int time){
        this.start = start;
        this.time = time;
    }
}