import java.util.ArrayList;

class Solution {

    public int[] solution(int n, long k) {
        int index = 0;
        int[] answer = new int[n];
        ArrayList<Integer> numbers = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            numbers.add(i + 1);
        }

        k -= 1;  // 0-index

        while (n > 0) {
            long mod = 1;
            for (int i = 1; i <= n - 1; i++) {
                mod *= i;
            }

            answer[index++] = numbers.remove((int) (k / mod));

            n -= 1;
            k %= mod;
        }

        return answer;
    }
}
