import java.util.*;
import java.util.stream.*;

class Solution {
    public int[][] solution(int n) {
        How[][][] hanoi = new How[4][4][n+1]; // [1,2,3]에서 [1,2,3]로 n개옮기는 방법
        
        How h = solve(1, 3, n);
        
        return h.get();
    }
    
    How solve(int from, int to, int n) {
        // from에서 to로 n개를 옮기는 방법
        if (n == 1) {
            How h = new How();
            h.add(from, to);
            return h;
        }
        
        if (from == to) throw new RuntimeException("???");
        
        int remain = 6 - to - from;
        How how = solve(from, remain, n-1);
        how.add(from, to);
        how.concat(solve(remain, to, n-1));
        return how;
    }
    
    static class How {
        List<Integer[]> how = new ArrayList<>();
        
        public int[][] get() {
            return how.stream().map(arr -> new int[]{arr[0], arr[1]}).toArray(int[][]::new);
        }
        
        public void add(int from, int to) {
            Integer[] h = new Integer[]{from, to};
            how.add(h);
        }
        
        public void concat(How how2) {
            this.how.addAll(how2.how);
        }
        
        public String toString() {
            return how.stream().map(Arrays::toString).collect(Collectors.joining(", "));
        }
    }
}