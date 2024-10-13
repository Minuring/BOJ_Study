import java.util.*;
class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {    
        int extIndex = columnToIndex(ext);
        int sortByIndex = columnToIndex(sort_by);
        
        return Arrays.stream(data)
            .filter(row -> row[extIndex] < val_ext)
            .sorted(Comparator.comparing(row -> row[sortByIndex]))
            .toArray(int[][]::new);
    }
    
    private int columnToIndex(String ext) {
        return switch (ext) {
            case "code"	-> 0;
            case "date" -> 1;
            case "maximum" -> 2;
            case "remain" -> 3;
            default -> -1;
        };
    }
}