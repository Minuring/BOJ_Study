import java.util.*;
import static java.util.stream.Collectors.*;

class Solution {
    public int solution(String[][] clothes) {
        for (String[] s : clothes) {
            String name = s[0];
            String kind = s[1];
        }
        Map<String, Long> counts = Arrays.stream(clothes)
            .collect(groupingBy(c -> c[1], counting()));

        Collection<Long> values = counts.values();
        int answer = 1;
        for(Long v : values) {
            answer *= (v+1);
        }
        
        return answer - 1;
    }
}