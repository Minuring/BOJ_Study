import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {

    public static final HashMap<Integer, TreeSet<Integer>> graph = new HashMap<Integer, TreeSet<Integer>>();

    public static void main(String[] args) {
        // 정점 번호 작은것 먼저. 1~N
        // 더 이상 없으면 종료.
        var scanner = new Scanner(System.in);
        var nmv = scanner.nextLine().split(" ");
        var n = Integer.parseInt(nmv[0]);
        var m = Integer.parseInt(nmv[1]);
        var v = Integer.parseInt(nmv[2]);

        // 양방향 간선 입력
        for (int i = 0; i < m; i++) {
            var split = scanner.nextLine().split(" ");
            var from = Integer.parseInt(split[0]);
            var to = Integer.parseInt(split[1]);

            add(from, to);
            add(to, from);
        }

        var visited = new boolean[n + 1];
        Arrays.fill(visited, false);
        printDFS(v, visited);
        System.out.println();

        Arrays.fill(visited, false);
        printBFS(v, visited);
    }

    private static void printDFS(int vertex, boolean[] visited) {
        System.out.print(vertex + " ");
        visited[vertex] = true;

        if (!graph.containsKey(vertex)) {
            return;
        }
        var connections = graph.get(vertex);
        for (var next : connections) {
            if (!visited[next]) {
                printDFS(next, visited);
            }
        }
    }

    private static void printBFS(int vertex, boolean[] visited) {
        Queue<Integer> q = new LinkedList<>();
        q.add(vertex);

        while (!q.isEmpty()) {
            var next = q.poll();
            if (visited[next]) {
                continue;
            }
            visited[next] = true;
            System.out.print(next + " ");

            var connections = graph.getOrDefault(next, new TreeSet<>());
            q.addAll(connections);
        }
    }

    private static void add(final int from, final int to) {
        if (graph.containsKey(from)) {
            graph.get(from).add(to);
        } else {
            var connections = new TreeSet<Integer>();
            connections.add(to);
            graph.put(from, connections);
        }
    }
}
