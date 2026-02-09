import java.util.*;

public class Main {

    private static int[][] board;
    private static int max = 0;
    private static int n = 0, m = 0;

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var split = scanner.nextLine().split(" ");
        n = Integer.parseInt(split[0]);
        m = Integer.parseInt(split[1]);

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            var row = scanner.nextLine().split(" ");
            for (var j = 0; j < row.length; j++) {
                board[i][j] = Integer.parseInt(row[j]);
            }
        }
        var put = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(put[i], false);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                var puts = new HashSet<Point>();
                puts.add(new Point(i, j));
                dfs(i, j, puts);
                puts.clear();
            }
        }

        System.out.println(max);
    }

    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    private static void dfs(int i, int j, Set<Point> puts) {
        if (puts.size() == 4) {
            int score = 0;
            for (var put : puts) {
                score += board[put.i][put.j];
            }
            max = Math.max(max, score);
            return;
        }

        if (puts.size() == 2) {
            var additionals = new ArrayList<Point>();
            for (int k = 0; k < 4; k++) {
                int ny = i + dy[k];
                int nx = j + dx[k];
                if (ny < 0 || ny >= n || nx < 0 || nx >= m) {
                    continue;
                }
                additionals.add(new Point(ny, nx));
            }
            for (int i1 = 0; i1 < additionals.size() - 1; i1++) {
                for (int i2 = i1 + 1; i2 < additionals.size(); i2++) {
                    var p1 = additionals.get(i1);
                    var p2 = additionals.get(i2);
                    if (!puts.contains(p1) && !puts.contains(p2)) {
                        puts.add(p1);
                        puts.add(p2);
                        dfs(p2.i, p2.j, puts);
                        puts.remove(p1);
                        puts.remove(p2);
                    }
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            int ny = i + dy[k];
            int nx = j + dx[k];
            if (ny < 0 || ny >= n || nx < 0 || nx >= m) {
                continue;
            }

            var point = new Point(ny, nx);
            if (puts.contains(point)) {
                continue;
            }

            puts.add(point);
            dfs(ny, nx, puts);
            puts.remove(point);
        }
    }

    private static class Point {
        int i;
        int j;

        public Point(int i, int j) {
            this.i = i;
            this.j = j;
        }

        @Override
        public final boolean equals(final Object o) {
            if (!(o instanceof Point)) {
                return false;
            }

            Point point = (Point) o;
            return i == point.i && j == point.j;
        }

        @Override
        public int hashCode() {
            int result = i;
            result = 31 * result + j;
            return result;
        }
    }
}
