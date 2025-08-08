import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		var line = br.readLine().split(" ");

		var n = Integer.parseInt(line[0]);
		var m = Integer.parseInt(line[1]);

		var metrix1 = createMetrix(n, m);
		var metrix2 = createMetrix(n, m);

		StringBuilder sb = new StringBuilder();
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				var sum = metrix1[i][j] + metrix2[i][j];
				sb.append(String.format("%d ", sum));
			}

			sb.append('\n');
		}

		System.out.print(sb);
	}

	static int[][] createMetrix(int n, int m) throws IOException {
		int[][] metrix = new int[n][m];
		
		for(int i=0; i<n; i++) {
			var elements = br.readLine().split(" ");
			var row = new int[m];
			for(int j=0; j<m; j++) {
				row[j] = Integer.parseInt(elements[j]);
			}

			metrix[i] = row;
		}

		return metrix;
	}
}