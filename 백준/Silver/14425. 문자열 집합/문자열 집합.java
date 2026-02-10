import java.util.HashSet;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var split = scanner.nextLine().split(" ");
        var n = Integer.parseInt(split[0]);
        var m = Integer.parseInt(split[1]);

        var s = new HashSet<String>();
        for (int i = 0; i < n; i++) {
            s.add(scanner.nextLine());
        }

        var count = 0;
        for (int i = 0; i < m; i++) {
            var str = scanner.nextLine();
            if (s.contains(str)) {
                count++;
            }
        }

        System.out.println(count);
    }
}