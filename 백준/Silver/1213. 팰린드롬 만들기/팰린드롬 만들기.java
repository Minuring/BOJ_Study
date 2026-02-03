import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var str = scanner.next();
        var chars = str.toCharArray();
        Arrays.sort(chars);

        var output = fillArr(chars);
        System.out.println(output);
    }

    private static String fillArr(final char[] chars) {
        var list = new ArrayList<Character>();
        var alone = ' ';
        for (int i = 0; i < chars.length; ) {
            if (i == chars.length - 1 || chars[i] != chars[i + 1]) {
                if (alone != ' ') {
                    return "I'm Sorry Hansoo";
                }
                alone = chars[i];
                i += 1;
            } else {
                list.add(chars[i]);
                i += 2;
            }
        }
        for (int i = list.size() - 1; i >= 0; i--) {
            list.add(list.get(i));
        }
        if (alone != ' ') {
            list.add(list.size() / 2, alone);
        }

        var sb = new StringBuilder();
        for (Character character : list) {
            sb.append(character);
        }
        return sb.toString();
    }
}
