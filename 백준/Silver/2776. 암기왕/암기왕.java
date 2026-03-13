import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        var scanner = new Scanner(System.in);
        var t = Integer.parseInt(scanner.nextLine());
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (var tc = 0; tc < t; tc++) {

            var n = Integer.parseInt(scanner.nextLine());
            var note1 = Arrays.stream(scanner.nextLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            Arrays.sort(note1);

            var m = Integer.parseInt(scanner.nextLine());
            var split = scanner.nextLine().split(" ");
            for (var num : split) {
                var i = Arrays.binarySearch(note1, Integer.parseInt(num));
                bw.write(i >= 0 ? "1\n" : "0\n");
            }
            bw.flush();
        }
    }
}
