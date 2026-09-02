class Solution {

    public long solution(int a, int b) {
        long answer = 0;
        int minNumber = Math.min(a, b);
        int maxNumber = Math.max(a, b);

        if ((long) a * (long) b < 0) {  // 두 개의 부호가 다르다면
            for (int i = Math.min(Math.abs(a), Math.abs(b)) + 1;
                i <= Math.max(Math.abs(a), Math.abs(b)); i++) {
                answer += i;
            }

            if (Math.abs(minNumber) > Math.abs(maxNumber)) {
                answer *= -1;
            }
        } else {  // 두 개의 부호가 같다면
            for (int i = minNumber; i <= maxNumber; i++) {
                answer += i;
            }
        }

        return answer;
    }
}
