import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class Main {

    public static List<Edge>[] graph;

    public static void main(String[] args) throws Exception {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var split = br.readLine().split(" ");
        var v = Integer.parseInt(split[0]);
        var e = Integer.parseInt(split[1]);
        var k = Integer.parseInt(br.readLine());
        graph = new List[v + 1];

        for (int i = 0; i < e; i++) {
            var spl = br.readLine().split(" ");
            var from = Integer.parseInt(spl[0]);
            var to = Integer.parseInt(spl[1]);
            var weight = Integer.parseInt(spl[2]);

            addEdge(from, to, weight);
        }

        var shortest = bfs(v, k);
        for (var x : shortest) {
            System.out.println(x != Integer.MAX_VALUE ? x : "INF");
        }
    }

    private static int[] bfs(final int v, final int k) {
        var pq = new PriorityQueue<Pair>((p1, p2) -> p1.dist - p2.dist);
        var dist = new int[v + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;
        pq.offer(new Pair(0, k));

        while (!pq.isEmpty()) {
            var pair = pq.poll();
            var vtx = pair.v;
            if (graph[vtx] == null || dist[vtx] < pair.dist) {
                continue;
            }

            var edges = graph[vtx];
            for (var e : edges) {
                if (dist[e.dest] > dist[vtx] + e.weight) {
                    dist[e.dest] = dist[vtx] + e.weight;
                    pq.offer(new Pair(dist[e.dest], e.dest));
                }
            }
        }
        return Arrays.copyOfRange(dist, 1, v + 1);
    }

    private static class Edge {
        int dest;
        int weight;

        public Edge(int d, int w) {
            dest = d;
            weight = w;
        }
    }

    private static class Pair {
        int dist;
        int v;

        public Pair(int dist, int v) {
            this.dist = dist;
            this.v = v;
        }
    }


    public static void addEdge(int from, int to, int weight) {
        if (graph[from] == null) {
            graph[from] = new ArrayList<>();
        }
        graph[from].add(new Edge(to, weight));
    }
}
