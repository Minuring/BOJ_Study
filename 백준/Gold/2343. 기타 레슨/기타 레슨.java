import java.util.Arrays;
import java.util.Scanner;

public class Main {

    private static final int MAX_BLUERAY_LEN = 100_000 * 10_000;
    private static int[] classes;

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var split = scanner.nextLine().split(" ");
        var n = Integer.parseInt(split[0]);
        var m = Integer.parseInt(split[1]);
        classes = Arrays.stream(scanner.nextLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int l = 1, r = MAX_BLUERAY_LEN;
        int mid = r / 2;
        while (l < r) {
            mid = (l + r) / 2;

            var requiredCount = test(mid);
            if (requiredCount > m) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        System.out.println(l);
    }

    private static int test(int brSize) {
        int usedCount = 1;
        int currentSize = 0;
        for (int aClass : classes) {
            if (currentSize + aClass <= brSize) {
                currentSize += aClass;
                continue;
            }

            usedCount += 1;
            if (aClass > brSize) {
                return Integer.MAX_VALUE;
            }
            currentSize = aClass;
        }
        return usedCount;
    }
}