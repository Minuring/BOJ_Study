import java.util.stream.*;
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Long> counts = Arrays.stream(participant).collect(Collectors.groupingBy(s -> s, Collectors.counting()));
        
        for(String s : completion) {
            counts.merge(s, counts.get(s) - 1, (old, young) -> young);
        }
        
        answer = counts.entrySet().stream().filter(e -> e.getValue() >= 1).map(e -> e.getKey()).findAny().orElseThrow();
        
        return answer;
    }
}