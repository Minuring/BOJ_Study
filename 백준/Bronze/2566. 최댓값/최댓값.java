import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		var br = new BufferedReader(new InputStreamReader(System.in));

		var max = Integer.MIN_VALUE;
		var maxR = 0;
		var maxC = 0;

		for(int r=0; r<9; r++) {
			var line = br.readLine().split(" ");
			for(int c=0; c<9; c++) {
				var n = Integer.parseInt(line[c]);
				if (n > max) {
					maxR = r;
					maxC = c;
					max = n;
				}
			}
		}

		System.out.printf("%d\n%d %d", max, maxR+1, maxC+1);
	}
}