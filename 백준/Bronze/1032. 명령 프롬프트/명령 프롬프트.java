import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var n = Integer.parseInt(scanner.nextLine());

        var pattern = scanner.nextLine().toCharArray();
        for (int i = 1; i < n; i++) {
            var name = scanner.nextLine();

            for (int j = 0; j < pattern.length; j++) {
                if (pattern[j] != name.charAt(j)) {
                    pattern[j] = '?';
                }
            }
        }

        var patternString = new String(pattern);
        System.out.println(patternString);
    }
}
