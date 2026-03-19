import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static List[] graph;
    private static int n;
    private static int m;

    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var split = br.readLine().split(" ");
        n = Integer.parseInt(split[0]);
        m = Integer.parseInt(split[1]);

        graph = new List[n + 1];
        for (var i = 0; i < n + 1; i++) {
            graph[i] = new ArrayList();
        }

        for (var i = 0; i < m; i++) {
            var spl = br.readLine().split(" ");
            var a = Integer.parseInt(spl[0]);
            var b = Integer.parseInt(spl[1]);
            var c = Integer.parseInt(spl[2]);
            graph[a].add(new Bridge(b, c));
            graph[b].add(new Bridge(a, c));
        }

        var spl = br.readLine().split(" ");
        var from = Integer.parseInt(spl[0]);
        var to = Integer.parseInt(spl[1]);

        System.out.println(dijkstra(from, to)[to]);
    }

    private static int[] dijkstra(int from, int to) {
        // weight 만큼을 한번에 이동시킬 수 있는가?
        class Pair {
            int limit, v;
            Pair(int _l, int _v) { v = _v; limit = _l; }
        }
        int[] limits = new int[n + 1];
        limits[from] = Integer.MAX_VALUE;

        var pq = new PriorityQueue<Pair>((p1, p2) -> p2.limit - p1.limit);
        pq.offer(new Pair(Integer.MAX_VALUE, from));
        while (!pq.isEmpty()) {
            var pair = pq.poll();
            if (limits[pair.v] > pair.limit) continue;

            for (var bridge : graph[pair.v]) {
                // 현재노드를 거쳤을 때 최대 한계 vs 기존 한계
                var limitOfThisPath = Math.min(limits[pair.v], ((Bridge) bridge).limit);
                var knownLimit = limits[((Bridge) bridge).to];
                if (limitOfThisPath > knownLimit) {
                    limits[((Bridge) bridge).to] = limitOfThisPath;
                    pq.offer(new Pair(limitOfThisPath, ((Bridge) bridge).to));
                }
            }
        }
        return limits;
    }

    private static class Bridge {
        public int to;
        public int limit;
        Bridge(int _to, int _limit) { to = _to; limit = _limit; }
    }
}
