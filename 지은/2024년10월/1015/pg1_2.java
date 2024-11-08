class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        
        int hap = 0;
        for(int i : arr) hap += i;
        
        answer = (double) hap / arr.length;
        return answer;
    }
}