import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var n = Integer.parseInt(scanner.nextLine());

        var dp = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            dp[i] = i;
        }

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j * j <= i; j++) {
                var square_j = 1 + dp[i - j * j];
                if (square_j < dp[i]) {
                    dp[i] = square_j;
                }
            }
        }
        System.out.println(dp[n]);
    }
}
