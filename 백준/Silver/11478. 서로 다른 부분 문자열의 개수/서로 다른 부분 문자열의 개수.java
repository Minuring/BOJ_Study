import java.util.HashSet;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var s = scanner.nextLine();

        var set = new HashSet<String>();
        for (int len = 1; len <= s.length(); len++) {
            for (int i = 0; i <= s.length() - len; i++) {
                var substr = s.substring(i, i + len);
                set.add(substr);
            }
        }

        System.out.println(set.size());
    }
}
