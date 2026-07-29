import java.util.ArrayDeque;

class Solution {

    static String makeBalancedP(String originStr) {
        if (originStr.length() == 0) {  // 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
            return "";
        }

        String u = "", v = "";

        ArrayDeque<Character> check = new ArrayDeque<>();
        int left = 0, right = 0;

        for (int i = 0; i < originStr.length(); i++) {  // 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
            if (originStr.charAt(i) == '(') {
                left += 1;

                check.addLast('(');
            } else {
                right += 1;

                if (check.size() != 0 && check.peekLast() == '(') {
                    check.removeLast();
                } else {
                    check.addLast(')');
                }
            }

            u += originStr.charAt(i);

            if (left == right) {  // 군형잡힌 괄호 문자열이라면 u와 v로 분리
                v = originStr.substring(i + 1, originStr.length());

                break;
            }
        }

        if (check.isEmpty()) {  // 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
            return u + makeBalancedP(v);
        }

        // 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
        String temp = "(";  // 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        temp += makeBalancedP(v);  // 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        temp += ")";  // 4-3. ')'를 다시 붙입니다.

        u = u.substring(1, u.length() - 1);  // 4-4. u의 첫 번째와 마지막 문자를 제거하고,

        for (int i = 0; i < u.length(); i++) {  // 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            if (u.charAt(i) == '(') {
                temp += ')';
            } else {
                temp += '(';
            }
        }

        return temp;  // 4-5. 생성된 문자열을 반환합니다.
    }

    public String solution(String p) {
        return makeBalancedP(p);
    }
}
