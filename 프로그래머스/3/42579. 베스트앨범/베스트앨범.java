import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Song> songs = new ArrayList<>();
        for(int i=0; i < genres.length; i++) {
            Song s = new Song(genres[i], plays[i], i);
            songs.add(s);
        }
        
        // plays의 합 기준 내림차순 정렬된 장르들
        List<String> genreOrder = songs.stream()
            .collect(groupingBy(s -> s.genre, summingInt(s -> s.plays)))
            .entrySet()
            .stream()
            .sorted(Comparator.comparing(Map.Entry<String, Integer>::getValue).reversed())
            .map(e -> ((Map.Entry<String,Integer>)e).getKey())
            .collect(Collectors.toList());
        
        // 장르 별 노래들
        Map<String, List<Song>> genreSongs = songs.stream().collect(groupingBy(s -> s.genre));
        List<Integer> ids = new ArrayList<>();
        for (String g : genreOrder) {
            List<Song> gs = genreSongs.get(g);
            gs.sort(Comparator.comparing(s -> ((Song)s).plays).reversed());
            
            int toIdx = Math.min(2, gs.size());
            List<Song> truncatedSongs = gs.subList(0, toIdx);
            truncatedSongs.forEach(s -> ids.add(s.id));
        }
        return ids.stream().mapToInt(Integer::intValue).toArray();
    }
    
    static class Song {
        public String genre;
        public int plays;
        public int id;
        
        public Song(String g, int p, int id) {
            genre = g;
            plays = p;
            this.id = id;
        }
    }
}