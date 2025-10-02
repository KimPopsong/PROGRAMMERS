import java.util.*;

class Solution {
    static Set<Integer> gates = new HashSet<>(), summits = new HashSet<>();
    static Map<Integer, Set<Path>> paths = new HashMap<>();

    public int[] solution(int n, int[][] pts, int[] gts, int[] sms) {
        // 초기화 시작

        for (int i = 1; i <= n; i++)  // paths 초기화
        {
            paths.put(i, new HashSet<>());
        }

        for (int[] p : pts)  // paths 초기화
        {
            paths.get(p[0]).add(new Path(p[1], p[2]));
            paths.get(p[1]).add(new Path(p[0], p[2]));
        }

        for (int i : gts)  // gates 초기화
        {
            gates.add(i);
        }

        for (int i : sms)  // summits 초기화
        {
            summits.add(i);
        }

        // 초기화 완료

        int[] distance = new int[n + 1];  // 시작 기준으로 노드 탐색
        Arrays.fill(distance, Integer.MAX_VALUE);

        dijkstra(distance);  // 탐색

        int summitNumber = Integer.MAX_VALUE, intensity = Integer.MAX_VALUE;  // 코스 탐색
        for (int ends : sms) {
            if (distance[ends] < intensity) {
                summitNumber = ends;
                intensity = distance[ends];
            } else if (distance[ends] == intensity && summitNumber > ends) {
                summitNumber = ends;
                intensity = distance[ends];
            }
        }

        return new int[]{summitNumber, intensity};
    }

    static void dijkstra(int[] distance) {
        PriorityQueue<Path> dijk = new PriorityQueue<>();

        for (int i : gates) {
            dijk.add(new Path(i, 0));
            distance[i] = 0;
        }

        while (!dijk.isEmpty()) {
            Path p = dijk.remove();

            if (p.dist > distance[p.dest]) {
                continue;
            }

            for (Path pp : paths.get(p.dest)) {
                if (gates.contains(pp.dest))  // 다른 시작점이라면
                {
                    continue;
                }

                int newDist = Math.max(p.dist, pp.dist);

                if (newDist < distance[pp.dest])  // 새로 찾은 경로의 intensity가 더 작다면
                {
                    distance[pp.dest] = newDist;

                    if (!summits.contains(pp.dest))  // 만약 정상이 아니라면
                    {
                        dijk.add(new Path(pp.dest, newDist));
                    }
                }
            }
        }
    }

    static class Path implements Comparable<Path> {
        int dest, dist;

        Path(int dest, int dist) {
            this.dest = dest;
            this.dist = dist;
        }

        @Override
        public int compareTo(Path p) {
            return Integer.compare(this.dist, p.dist);
        }
    }
}
