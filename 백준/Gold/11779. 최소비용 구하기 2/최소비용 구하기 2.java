import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

public class Main {

    private static int n;
    private static List[] graph;

    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new List[n + 1];
        for (var i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<Edge>();
        }

        var m = Integer.parseInt(br.readLine());
        for (var i = 0; i < m; i++) {
            var split = br.readLine().split(" ");
            var from = Integer.parseInt(split[0]);
            var to = Integer.parseInt(split[1]);
            var weight = Integer.parseInt(split[2]);
            graph[from].add(new Edge(to, weight));
        }

        var fromAndTo = br.readLine().split(" ");
        var from = Integer.parseInt(fromAndTo[0]);
        var to = Integer.parseInt(fromAndTo[1]);

        dijkstra(from, to);
    }

    private static void dijkstra(int start, int end) {
        class Pair {
            final int dist, v;

            Pair(int d, int v) {
                dist = d;
                this.v = v;
            }
        }

        var dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        var before = new int[n + 1];
        Arrays.fill(before, -1);

        var pq = new PriorityQueue<Pair>((p1, p2) -> p1.dist - p2.dist);
        pq.offer(new Pair(0, start));

        while (!pq.isEmpty()) {
            var pair = pq.poll();
            if (dist[pair.v] < pair.dist) {
                continue;
            }

            for (Object e : graph[pair.v]) {
                var linkedV = ((Edge) e).to;
                var linkedW = ((Edge) e).weight;
                if (dist[linkedV] > dist[pair.v] + linkedW) {
                    dist[linkedV] = dist[pair.v] + linkedW;
                    before[linkedV] = pair.v;
                    pq.offer(new Pair(dist[linkedV], linkedV));
                }
            }
//            System.out.printf("pair{v=%d, dist=%d} 처리 후 dist배열 = %s, before배열 = %s\n", pair.v, pair.dist, Arrays.toString(dist), Arrays.toString(before));
        }

        var path = new ArrayList<Integer>();
        for (int x = end; x != -1; x = before[x]) {
            path.add(x);
        }

        System.out.println(dist[end]);
        System.out.println(path.size());
        var sb = new StringBuilder();
        for (int i = path.size() - 1; i >= 0; i--) {
            sb.append(path.get(i));
            if (i > 0) sb.append(" ");
        }
        System.out.println(sb);
    }

    private static class Edge {
        int to;
        int weight;

        public Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }
}
