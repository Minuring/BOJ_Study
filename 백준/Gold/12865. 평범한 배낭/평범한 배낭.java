import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] split = scanner.nextLine().split(" ");
        int N = Integer.parseInt(split[0]);
        int K = Integer.parseInt(split[1]);

        List<Thing> things = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] split2 = scanner.nextLine().split(" ");
            Thing thing = new Thing(Integer.parseInt(split2[0]), Integer.parseInt(split2[1]));
            things.add(thing);
        }

        int[][] dp = new int[N + 1][K + 1]; // dp[n][w] = 물건 n번째까지, 가방 최대용량이 w일 때 최대 value
        for (int n = 1; n <= N; n++) {
            Thing thing = things.get(n - 1);

            for (int w = 1; w <= K; w++) {

                if (thing.weight <= w) {
                    dp[n][w] = Math.max(dp[n - 1][w], dp[n - 1][w - thing.weight] + thing.value);
                } else {
                    dp[n][w] = dp[n - 1][w];
                }

            }
        }

        System.out.println(dp[N][K]);
    }

    static class Thing {
        public int weight;
        public int value;

        public Thing(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }
}