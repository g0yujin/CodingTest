import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        boolean check = false;
        for(int i=0; i<numbers.length; i++) {
            if(numbers[i] != 0) check = true;
        }
        
        if(!check) return "0";
        
        String[] arr = new String[numbers.length];
        for(int i=0; i<arr.length; i++) {
            arr[i] = String.valueOf(numbers[i]);
        }
        Arrays.sort(arr, (o1, o2) -> {
            String s1 = o1+o2;
            String s2 = o2+o1;
            
            return s2.compareTo(s1);
        });
        
        StringBuilder sb = new StringBuilder();
        for(String s : arr) {
            sb.append(s);
        }
        return sb.toString();
    }
}