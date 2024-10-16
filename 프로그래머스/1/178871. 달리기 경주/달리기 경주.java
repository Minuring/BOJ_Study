import java.util.HashMap;
import java.util.Comparator;

class Solution {
    HashMap<String, Integer> strToInt = new HashMap<>();
    
    public String[] solution(String[] players, String[] callings) {
        for(int i=0; i<players.length; i++) {
            strToInt.put(players[i], i);
        }
        
        for(String name : callings) {
            call(players, name);
        }
        return strToInt.keySet()
            .stream()
            .sorted(Comparator.comparing(strToInt::get))
            .toArray(String[]::new);
    }
    
    private void call(String[] players, String name) {
        int i = strToInt.get(name);
        String target = players[i-1];
        
        players[i] = target;
        strToInt.replace(target, i);
        
        players[i-1] = name;
        strToInt.replace(name, i-1);
    }
    
}