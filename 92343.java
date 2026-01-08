import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {

    int answer = 1;
    int[] info;  // 0은 양, 1은 늑대
    Map<Integer, Set<Integer>> edges = new HashMap<>();

    public int solution(int[] info, int[][] ed) {
        this.info = info;

        for (int i = 0; i < info.length; i++) {
            edges.put(i, new HashSet<>());
        }

        for (int[] e : ed) {
            edges.get(e[0]).add(e[1]);
            edges.get(e[1]).add(e[0]);
        }

        boolean[] isVisit = new boolean[info.length];
        Set<Integer> queue = new HashSet<>();

        dfs(1 + findAdjacentSheep(0, isVisit, queue), 0, isVisit, queue);

        return answer;
    }

    /**
     * 인접한 양 모두 찾기
     *
     * @param startNode 찾기 시작하는 양의 위치
     * @param isVisit   방문 여부
     * @param queue     탐색해야하는 늑대의 위치
     * @return 찾은 양
     */
    int findAdjacentSheep(int startNode, boolean[] isVisit, Set<Integer> queue) {
        int sheepNumber = 0;

        ArrayDeque<Integer> findSheep = new ArrayDeque<>();
        isVisit[startNode] = true;
        findSheep.add(startNode);

        while (!findSheep.isEmpty()) {
            int node = findSheep.removeFirst();

            for (int e : edges.get(node)) {
                if (!isVisit[e]) {
                    if (info[e] == 0) {  // 양
                        isVisit[e] = true;
                        sheepNumber += 1;
                        findSheep.addLast(e);
                    } else {  // 늑대
                        queue.add(e);
                    }
                }
            }
        }

        return sheepNumber;
    }

    void dfs(int sheep, int wolf, boolean[] isVisit, Set<Integer> queue) {
        answer = Math.max(answer, sheep);

        for (int node : queue) {
            if (isVisit[node]) {
                continue;
            }

            if (sheep <= wolf + 1) {
                continue;
            }

            boolean[] newVisit = isVisit.clone();
            Set<Integer> newQueue = new HashSet<>(queue);

            dfs(sheep + findAdjacentSheep(node, newVisit, newQueue), wolf + 1, newVisit, newQueue);
        }
    }
}
