class Solution {

    static int answer;

    public int solution(String name) {
        for (int i = 0; i < name.length(); i++) {  // 상하 이동 계산
            int diff = name.charAt(i) - 'A';

            answer += Math.min(26 - diff, diff);
        }

        int move = name.length() - 1;  // 오른쪽으로만 이동하는 경우

        for (int i = 0; i < name.length(); i++) {
            int next = i + 1;

            while (next < name.length() && name.charAt(next) == 'A') {
                next++;
            }

            int rightFirst = i * 2 + name.length() - next;
            int leftFirst = (name.length() - next) * 2 + i;

            move = Math.min(move, rightFirst);
            move = Math.min(move, leftFirst);
        }

        return answer + move;
    }
}
