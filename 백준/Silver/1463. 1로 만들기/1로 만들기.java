import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var n = Integer.parseInt(scanner.nextLine());

        System.out.println(solve(n));
    }
    
    static int solve(int x) {
        int[] memo = new int[x + 1];
        Arrays.fill(memo, Integer.MAX_VALUE);
        memo[0] = memo[1] = 0;
        
        for (int i = 2; i < x + 1; i++) {
            if (i % 3 == 0) {
                memo[i] = Math.min(memo[i], memo[i / 3] + 1);
            }
            if (i % 2 == 0) {
                memo[i] = Math.min(memo[i], memo[i / 2] + 1);
            }
            memo[i] = Math.min(memo[i], memo[i - 1] + 1);
        }
        return memo[x];
    }
}
