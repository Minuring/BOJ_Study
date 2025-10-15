

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static final Scanner SC = new Scanner(System.in);
    static int N;
    static long[] As;

    public static void main(String[] args) {
        N = Integer.parseInt(SC.nextLine());
        As = Arrays.stream(SC.nextLine().split(" "))
                .mapToLong(Long::parseLong)
                .toArray();

        Arrays.sort(As);

        int count = 0;
        for (int i = 0; i < N; i++) {
            int left = 0;
            int right = N - 1;

            while (left < right) {
                if (left == i) {
                    left++;
                    continue;
                }
                if (right == i) {
                    right--;
                    continue;
                }

                long sum = As[left] + As[right];
                if (sum == As[i]) {
                    count++;
                    break;
                } else if (sum < As[i]) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        System.out.println(count);
    }
}
