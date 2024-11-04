import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int[] arrCpy = arr.clone();
        int[] answer = new int[arr.length-1];
        Arrays.sort(arrCpy);
        int index = 0;
        for(int i=0; i<arr.length; i++) {
            if(arrCpy[0] != arr[i]) {
                answer[index] = arr[i];
                index++;
            }
        }
        return answer.length == 0 ? new int[]{-1} : answer;
    }
}