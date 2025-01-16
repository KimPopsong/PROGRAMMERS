import java.util.*;
import java.io.*;

class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			int numSum = 0;
			String[] numberTemp = br.readLine().split(" ");

			for (String num : numberTemp) {
				int n = Integer.parseInt(num);

				if (n % 2 == 1) {
					numSum += n;
				}
			}

			sb.append("#").append(tc).append(" ").append(numSum).append("\n");
		}

		System.out.println(sb);
	}
}
