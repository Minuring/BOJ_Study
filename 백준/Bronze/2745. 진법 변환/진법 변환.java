import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        char[] chars = split[0].toCharArray();

        int base = Integer.parseInt(split[1]);
        
        long sum = 0;
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (c >= 'A' && c <= 'Z') {
                int number = (c - 'A') + 10;
                sum += (long) Math.pow(base, chars.length -i -1) * number;
            } else {
                sum += (long) Math.pow(base, chars.length -i -1) * (c - '0');
            }
        }

        System.out.println(sum);
    }
}