import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {
        var reader = new BufferedReader(new InputStreamReader(System.in));
        var split = reader.readLine().split(" ");
        var n = Integer.parseInt(split[0]);
        var m = Integer.parseInt(split[1]);

        var parents = new int[n + 1];
        var depth = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parents[i] = i;
            depth[i] = 0;
        }

        for (int i = 0; i < m; i++) {
            var spl = reader.readLine().split(" ");
            var operation = spl[0];
            var operand1 = Integer.parseInt(spl[1]);
            var operand2 = Integer.parseInt(spl[2]);
            if (operation.equals("0")) {
                // union 1,2
                var p1 = findParent(parents, operand1);
                var p2 = findParent(parents, operand2);
                if (p1 == p2) {
                    continue;
                }

                if (depth[p1] > depth[p2]) {
                    parents[p2] = parents[p1];
                } else if (depth[p1] < depth[p2]) {
                    parents[p1] = parents[p2];
                } else {
                    parents[p2] = parents[p1];
                    depth[p1] += 1;
                }

            } else {
                // check
                var p1 = findParent(parents, operand1);
                var p2 = findParent(parents, operand2);
                System.out.println(p1 == p2 ? "YES" : "NO");
            }
        }
    }

    private static int findParent(int[] parents, int i) {
        while (parents[i] != i) {
            var tmp = i;
            i = parents[i];
            parents[tmp] = parents[i];
        }
        return i;
    }
}
