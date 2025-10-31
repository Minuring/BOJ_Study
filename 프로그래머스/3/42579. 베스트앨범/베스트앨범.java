import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.*;
import static java.util.Comparator.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        return IntStream.range(0, genres.length)
            .mapToObj(i -> new Song(genres[i], plays[i], i))
            .collect(groupingBy(s -> s.genre)) // Map<String, List<Song>>
            .entrySet().stream() // Stream<Map.Entry<String, List<Song>>>
            .sorted(comparingInt(e -> e.getValue().stream().mapToInt(s -> s.plays).sum() * -1))
            .flatMap(e -> e.getValue().stream().sorted().limit(2)) // Stream<Song>
            .mapToInt(s -> s.id)
            .toArray();
    }
    
    static class Song implements Comparable<Song> {
        public String genre;
        public int plays;
        public int id;
        
        public Song(String g, int p, int id) {
            genre = g;
            plays = p;
            this.id = id;
        }
        
        public int compareTo(Song other) {
            int comp = Integer.compare(other.plays, this.plays);
            if (comp != 0) return comp;
            return Integer.compare(this.id, other.id);
        }
    }
}