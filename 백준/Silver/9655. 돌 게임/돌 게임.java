import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var n = Integer.parseInt(scanner.nextLine());

        // 게임이 끝나는 턴 수
        int[] dp = new int[1001];
        dp[0] = 0;
        dp[1] = 1; //sk1
        dp[2] = 2; //sk1-cy1
        dp[3] = 1; //sk3
        for (int i = 4; i < n + 1; i++) {
            dp[i] = Math.min(dp[i - 1], dp[i - 3]) + 1;
        }
        System.out.println(dp[n] % 2 == 1 ? "SK" : "CY");
    }
}
