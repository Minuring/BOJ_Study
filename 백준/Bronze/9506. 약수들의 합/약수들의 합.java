import static java.util.stream.Collectors.joining;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int input = sc.nextInt();
            if (input == -1) {
                break;
            }

            List<Integer> list = yaksuWithoutSelf(input);
            int sum = list.stream().mapToInt(i -> i).sum();
            if (sum == input) {
                System.out.print(input + " = ");
                String sumExpression = list.stream().map(String::valueOf).collect(joining(" + "));
                System.out.println(sumExpression);
            } else {
                System.out.println(input + " is NOT perfect.");
            }
        }
    }

    private static List<Integer> yaksuWithoutSelf(int n) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        for(int i=2; i<n; i++) {
            if (n % i == 0) {
                list.add(i);
            }
        }
        return list;
    }
}