import java.util.Scanner;
import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var str = scanner.nextLine();
        var bomb = scanner.nextLine();

        var stack = new Stack<Character>();
        var chars = str.toCharArray();
        for (var ch : chars) {
            stack.push(ch);
            var flag = true;
            while (stack.size() >= bomb.length() && flag) {
                // 마지막에 폭탄 문자열 있는 지 확인
                for (int i = 0; i < bomb.length(); i++) {
                    var i_stack = stack.size() - bomb.length() + i;
                    if (stack.get(i_stack) != bomb.charAt(i)) {
                        flag = false;
                        break;
                    }
                }
                // 제거
                if (flag) {
                    for (int i = 0; i < bomb.length(); i++) {
                        stack.pop();
                    }
                }
            }
        }

        var sb = new StringBuilder();
        for (var ch : stack) {
            sb.append(ch);
        }
        var result = sb.toString();
        System.out.println(result.isEmpty() ? "FRULA" : result);
    }
}
