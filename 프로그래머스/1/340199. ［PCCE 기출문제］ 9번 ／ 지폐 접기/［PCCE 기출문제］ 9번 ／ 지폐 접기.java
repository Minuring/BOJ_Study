class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        while(min(wallet) < min(bill) || max(wallet) < max(bill)) {
            if (bill[0] >= bill[1]) bill[0] /= 2;
            else bill[1] /= 2;
            answer++;
        }
        
        return answer;
    }
    
    private int min(int[] arr){
        return arr[0] >= arr[1] ? arr[1] : arr[0];
    }
    
    private int max(int[] arr){
        return arr[0] >= arr[1] ? arr[0] : arr[1];
    }
}