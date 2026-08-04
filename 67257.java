import java.util.ArrayDeque;
import java.util.ArrayList;

class Solution {

    static long answer = 0;
    static char[] operation = {'+', '-', '*'};
    static ArrayList<String> originExpression = new ArrayList<>();

    static void pickOperationOrder(ArrayList<Character> op, boolean[] isVisit, int depth) {
        if (depth == 3) {  // 계산
            calcBiggestValue(op);
        }

        for (int i = 0; i < 3; i++) {
            if (isVisit[i] == false) {
                isVisit[i] = true;
                op.addLast(operation[i]);

                pickOperationOrder(op, isVisit, depth + 1);

                isVisit[i] = false;
                op.removeLast();
            }
        }
    }

    static void calcBiggestValue(ArrayList<Character> op) {
        int opIndex = 0;
        ArrayDeque<String> expression = new ArrayDeque<>(originExpression);
        ArrayDeque<String> temp = new ArrayDeque<>();

        while (temp.size() + expression.size() != 1) {
            while (!expression.isEmpty()) {
                String t = expression.removeFirst();

                if (t.length() == 1 && t.charAt(0) == op.get(opIndex)) {  // 수식
                    Long num1 = Long.parseLong(temp.removeLast());
                    Long num2 = Long.parseLong(expression.removeFirst());

                    if (op.get(opIndex) == '+') {
                        t = String.valueOf(num1 + num2);
                    } else if (op.get(opIndex) == '-') {
                        t = String.valueOf(num1 - num2);
                    } else {
                        t = String.valueOf(num1 * num2);
                    }
                }

                temp.addLast(t);
            }

            ArrayDeque<String> swap = expression;
            expression = temp;
            temp = swap;

            opIndex += 1;
        }

        answer = Math.max(answer, Math.abs(Long.parseLong(expression.removeFirst())));
    }

    public long solution(String expression) {
        String temp = "";
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);

            if (c == '+' || c == '-' || c == '*') {
                originExpression.addLast(temp);
                originExpression.addLast(Character.toString(c));

                temp = "";
            } else {
                temp += c;
            }
        }
        originExpression.addLast(temp);

        pickOperationOrder(new ArrayList<>(), new boolean[3], 0);

        return answer;
    }
}
