import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static int n, m;
    static int[][] MAP;

    public static void main(String[] args) {
        final var scanner = new Scanner(System.in);
        final var split = scanner.nextLine().split(" ");
        n = Integer.parseInt(split[0]);
        m = Integer.parseInt(split[1]);

        MAP = new int[n][m];
        for (int i = 0; i < n; i++) {
            MAP[i] = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        for (int year = 0; ; year++) {
            // 덩어리 2개 이상이면 끝
            final var count = count();
            if (count >= 2) {
                System.out.println(year);
                return;
            }
            if (count == 0) {
                System.out.println(0);
                return;
            }

            // 녹이기
            melt();
        }
    }

    private static void melt() {

        final var poses = new ArrayList<Pos>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (MAP[i][j] == 0) {
                    poses.add(new Pos(i, j));
                }
            }
        }

        for (final var pos : poses) {
            if (pos.i - 1 >= 0 && MAP[pos.i - 1][pos.j] >= 1) {
                MAP[pos.i - 1][pos.j] -= 1;
            }
            if (pos.i + 1 < MAP.length && MAP[pos.i + 1][pos.j] >= 1) {
                MAP[pos.i + 1][pos.j] -= 1;
            }
            if (pos.j - 1 >= 0 && MAP[pos.i][pos.j - 1] >= 1) {
                MAP[pos.i][pos.j - 1] -= 1;
            }
            if (pos.j + 1 < MAP[0].length && MAP[pos.i][pos.j + 1] >= 1) {
                MAP[pos.i][pos.j + 1] -= 1;
            }
        }
    }

    private static int count() {
        int[][] check = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(check[i], 0);
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                count += dfs(check, i, j) > 0 ? 1 : 0;
            }
        }
        return count;
    }

    private static int dfs(int[][] check, int i, int j) {
        if (i < 0 || i >= n || j < 0 || j >= m) {
            return 0;
        }

        // 잠겨있거나 이미 확인했으면
        if (MAP[i][j] == 0 || check[i][j] == 1) {
            return 0;
        }

        check[i][j] = 1;
        return 1 + dfs(check, i - 1, j)
                + dfs(check, i + 1, j)
                + dfs(check, i, j - 1)
                + dfs(check, i, j + 1);
    }

    static class Pos {
        int i;
        int j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}