import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var s = new StringBuilder(scanner.nextLine());
        var t = new StringBuilder(scanner.nextLine());

        while (s.length() < t.length()) {
            var last_t = t.charAt(t.length() - 1);
            t = t.deleteCharAt(t.length() - 1);

            if (last_t == 'B') {
                t = t.reverse();
            }
        }

        var ans = s.toString().contentEquals(t);
        System.out.println(ans ? 1 : 0);
    }
}
