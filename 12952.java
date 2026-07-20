import java.util.HashSet;
import java.util.Set;

class Solution {

    static int mapSize, answer;
    static Set<Integer> colSet, dig1Set, dig2Set;

    static void dfs(int depth, int queenNumber) {
        if (depth >= mapSize) {
            if (queenNumber == mapSize) {
                answer += 1;
            }

            return;
        }

        for (int c = 0; c < mapSize; c++) {
            if (colSet.contains(c)) {
                continue;
            } else if (dig1Set.contains(c - depth)) {
                continue;
            } else if (dig2Set.contains(depth + c)) {
                continue;
            } else {  // 조건 충족
                colSet.add(c);
                dig1Set.add(c - depth);
                dig2Set.add(depth + c);

                dfs(depth + 1, queenNumber + 1);

                dig2Set.remove(depth + c);
                dig1Set.remove(c - depth);
                colSet.remove(c);
            }
        }
    }

    public int solution(int n) {
        mapSize = n;

        colSet = new HashSet<>();
        dig1Set = new HashSet<>();
        dig2Set = new HashSet<>();

        dfs(0, 0);

        return answer;
    }
}
