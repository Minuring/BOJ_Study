import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {

    static final Scanner SC = new Scanner(System.in);
    static int N;
    static long[] As;

    public static void main(String[] args) {
        input();

        Arrays.sort(As);

        long count = IntStream.range(0, N)
                .filter(i -> isGoodNumber(i))
                .count();

        System.out.println(count);
    }

    private static boolean isGoodNumber(int numberIdx) {
        int left = 0;
        int right = N - 1;

        while (left < right) {
            if (left == numberIdx) {
                left++;
                continue;
            }
            if (right == numberIdx) {
                right--;
                continue;
            }

            long sum = As[left] + As[right];
            if (sum == As[numberIdx]) {
                return true;
            } else if (sum < As[numberIdx]) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }

    private static void input() {
        N = Integer.parseInt(SC.nextLine());
        As = Arrays.stream(SC.nextLine().split(" "))
                .mapToLong(Long::parseLong)
                .toArray();
    }
}
