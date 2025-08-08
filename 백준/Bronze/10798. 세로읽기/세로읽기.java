import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));

        var arr = new ArrayList<char[]>();
        var maxLength = 0;
        while(true) {
            var line = br.readLine();
            if (line == null) break;

            var chars = line.toCharArray();
            maxLength = Math.max(maxLength, chars.length);
            arr.add(chars);
        }

        var sb = new StringBuilder();
        for(int c=0; c<maxLength; c++) {
            for(int r=0; r<5; r++) {
                if (arr.get(r).length <= c) continue;
                sb.append(arr.get(r)[c]);
            }
        }

        System.out.print(sb);
    }
}