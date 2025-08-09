import java.util.*;

class Solution {
    static Map<Integer, Map<Integer, Integer>> distances = new HashMap<>();

    public int[] solution(int n, int[][] roads, int[] sources, int destination)
    {
        int[] answer = new int[sources.length];

        for (int i = 1; i <= n; i++)
        {
            distances.put(i, new HashMap<>());
        }

        for (int[] r : roads)
        {
            distances.get(r[0]).put(r[1], 1);
            distances.get(r[1]).put(r[0], 1);
        }

        // destination에 대해 최단거리 계산

        int count = 1;
        boolean[] isVisit = new boolean[n + 1];
        PriorityQueue<Location> djk = new PriorityQueue<>();

        djk.add(new Location(0, destination));

        while (!djk.isEmpty() && (count <= n))
        {
            Location l = djk.remove();

            if (isVisit[l.destination])  // 이미 방문하였다면
            {
                continue;  // 생략
            }

            count += 1;
            isVisit[l.destination] = true;
            distances.get(destination).put(l.destination, l.distance);

            Map<Integer, Integer> dis = distances.get(l.destination);

            for (int k : dis.keySet())
            {
                if (isVisit[k])
                {
                    continue;
                }

                djk.add(new Location(l.distance + dis.get(k), k));
            }
        }

        for (int i = 0; i < sources.length; i++)
        {
            if (distances.get(destination).get(sources[i]) != null)
            {
                answer[i] = distances.get(destination).get(sources[i]);
            }

            else
            {
                answer[i] = -1;
            }
        }

        return answer;
    }

    static class Location implements Comparable<Location> {
        int distance, destination;

        public Location(int distance, int destination)
        {
            this.distance = distance;
            this.destination = destination;
        }

        @Override
        public int compareTo(Location l)
        {
            return Integer.compare(this.distance, l.distance);
        }
    }
}
