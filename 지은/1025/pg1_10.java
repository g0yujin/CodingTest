class Solution {
    public boolean solution(int x) {
        int temp = x;
        int hap = 0;
        while(temp>0) {
            hap += temp%10;
            temp = temp/10;
        }
        
        return x % hap == 0 ? true : false;
    }
}