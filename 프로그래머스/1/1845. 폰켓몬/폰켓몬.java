import java.util.*;
import static java.util.stream.Collectors.*;

class Solution {
    public int solution(int[] nums) {
        Map<Integer, Long> counts = Arrays.stream(nums)
            .boxed()
            .collect(groupingBy(i -> i, counting()));
        
        int speciesCount = counts.keySet().size();
        int n = nums.length / 2;
        
        if (speciesCount >= n) return n;
        return speciesCount;
    }
}