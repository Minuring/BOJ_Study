import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        Map<String, Map<String, Integer>> outerMap = toMatrix(friends);
        Map<String, Integer> giftScoreMap = new HashMap<>();
        for (String friend : friends) {
            giftScoreMap.put(friend, 0);
        }
        applyGifts(outerMap, gifts, giftScoreMap);
        
        Map<String, Integer> receiveMap = Arrays.stream(friends)
            .collect(Collectors.toMap(s -> s, s -> 0));
        Set<String> checked = new HashSet<>();
        
        for(String a : outerMap.keySet()) {
            Map<String,Integer> innerMap = outerMap.get(a);
            for(String b : innerMap.keySet()) {
                if(a.equals(b)) continue;
                if(checked.contains(a.concat(b))
                   || checked.contains(b.concat(a))) continue;
                else checked.add(a.concat(b));
                
                Integer aToB = innerMap.get(b);
                Integer bToA = outerMap.get(b).get(a);
                if (aToB == bToA) {
                    //선물지수
                    Integer scoreA = giftScoreMap.get(a);
                    Integer scoreB = giftScoreMap.get(b);
                    if (scoreA == scoreB) continue;
                    
                    String higher = scoreA > scoreB ? a : b;
                    Integer oldScore = receiveMap.get(higher);
                    receiveMap.replace(higher, oldScore + 1);
                } else {
                    String whoGaveMore = aToB > bToA ? a : b;
                    Integer oldValue = receiveMap.get(whoGaveMore);
                    receiveMap.replace(whoGaveMore, oldValue + 1);
                }
            }
        }
        
        Integer answer = receiveMap.values().stream().max(Comparator.naturalOrder()).orElse(0);
        return answer;
    }
    
    private Map<String, Map<String, Integer>> toMatrix(String[] friends){
        Map<String, Map<String, Integer>> outerMap = new HashMap<>();
        
        for(String f1 : friends) {
            Map<String, Integer> innerMap = new HashMap<>();
            
            for(String f2 : friends) {
                if (f1.equals(f2)) continue;
                innerMap.put(f2, 0);
            }
            outerMap.put(f1, innerMap);
        }
        
        return outerMap;
    }
    
    private void applyGifts(Map<String, Map<String, Integer>> map, String[] gifts
                            , Map<String, Integer> giftScoreMap) {
        for(String gift : gifts) {
            String[] splited = gift.split(" ");
            String A = splited[0];
            String B = splited[1];
            
            Map<String, Integer> innerMap = map.get(A);
            Integer oldValue = innerMap.get(B);
            innerMap.replace(B, oldValue + 1);
            
            Integer oldScoreA = giftScoreMap.get(A);
            Integer oldScoreB = giftScoreMap.get(B);
            giftScoreMap.replace(A, oldScoreA + 1);
            giftScoreMap.replace(B, oldScoreB - 1);
        }
    }
}