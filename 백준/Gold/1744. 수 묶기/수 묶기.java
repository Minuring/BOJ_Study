import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var n = Integer.parseInt(scanner.nextLine());

        var negatives = new PriorityQueue<Integer>();
        var zeros = 0;
        var positives = new PriorityQueue<Integer>(Comparator.reverseOrder());
        for (int i = 0; i < n; i++) {
            var x = Integer.parseInt(scanner.nextLine());
            if (x < 0) negatives.add(x);
            else if (x > 0) positives.add(x);
            else zeros++;
        }

        int sum = 0;
        while (negatives.size() >= 2) {
            sum += negatives.poll() * negatives.poll();
        }
        while (positives.size() >= 2) {
            var a = positives.poll();
            var b = positives.poll();
            sum += (a > 2 && b > 1) ? (a * b) : (a + b);
        }

        if (!negatives.isEmpty()) {
            if (zeros == 0) {
                sum += negatives.poll();
            }
            // else merge with zero
        }
        if (!positives.isEmpty()) {
            sum += positives.poll();
        }

        System.out.println(sum);
    }
}
