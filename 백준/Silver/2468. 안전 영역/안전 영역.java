import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static final Scanner scanner = new Scanner(System.in);

    static int N;
    static int[][] map;

    public static void main(String[] args) {
        N = Integer.parseInt(scanner.nextLine());
        map = createMap();
        int maxCount = 0;

        for (int waterH = 0; waterH <= 100; waterH++) {
            var count = countArea(waterH);
            maxCount = Math.max(count, maxCount);
        }

        System.out.println(maxCount);
    }

    private static int countArea(final int waterH) {
        final var check = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(check[i], -1);
        }

        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                
                if (check[i][j] != -1) continue; // 이미 확인했으면 건너뛰고
                count += dfs(i, j, waterH, check) >= 1 ? 1 : 0;
                
            }
        }
        return count;
    }

    private static int dfs(int i, int j, int waterH, int[][] check) {
        // 맵 밖이면 out
        if (i < 0 || i >= N || j < 0 || j >= N) return 0;

        // 이미 확인했으면 return
        if (check[i][j] != -1) return check[i][j];

        if (map[i][j] > waterH) { // 안 잠기면
            check[i][j] = 1;

            dfs(i - 1, j, waterH, check); // 상
            dfs(i + 1, j, waterH, check); // 하
            dfs(i, j - 1, waterH, check); // 좌
            dfs(i, j + 1, waterH, check); // 우

            return 1;

        } else { // 잠기면
            check[i][j] = 0;
            return 0;
        }
    }

    private static int[][] createMap() {
        int[][] map = new int[N][N];
        for (int i = 0; i < N; i++) {
            final var split = scanner.nextLine().split(" ");
            map[i] = Arrays.stream(split)
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
        return map;
    }
}