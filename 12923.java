class Solution {

    public int[] solution(long begin, long end) {
        int gap = (int) (end - begin);
        int[] answer = new int[gap + 1];

        for (long i = begin; i <= end; i++) {
            if (i == 1) {
                answer[(int) (i - begin)] = 0;

                continue;
            }

            int num = 1;

            for (long j = 2; j * j <= i; j++) {
                if (i % j == 0) {  // 나누어 떨어진다면
                    if (i / j <= 10000000) {
                        num = (int) (i / j);

                        break;
                    } else {
                        num = (int) j;
                    }
                }
            }

            answer[(int) (i - begin)] = num;
        }

        return answer;
    }
}
