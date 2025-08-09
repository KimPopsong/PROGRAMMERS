import java.util.*;

class Solution {
    static boolean[][] graph, map;

    public int solution(int playerNumber, int[][] edges)
    {
        int answer = 0;

        graph = new boolean[playerNumber + 1][playerNumber + 1];
        map = new boolean[playerNumber + 1][playerNumber + 1];

        for (int[] e : edges)
        {
            graph[e[0]][e[1]] = true;
        }

        for (int p = 1; p <= playerNumber; p++)
        {
            ArrayDeque<Integer> bfs = new ArrayDeque<>();
            bfs.add(p);

            while (!bfs.isEmpty())
            {
                int pp = bfs.remove();

                graph[p][pp] = true;

                for (int i = 1; i <= playerNumber; i++)
                {
                    if (graph[pp][i] && !map[p][i])
                    {
                        map[p][i] = true;

                        bfs.add(i);
                    }
                }
            }
        }

        for (int i = 1; i <= playerNumber; i++)
        {
            for (int j = 1; j <= playerNumber; j++)
            {
                if (map[i][j])
                {
                    map[j][i] = true;
                }
            }
        }

        for (int i = 1; i <= playerNumber; i++)
        {
            boolean flag = true;

            for (int j = 1; j <= playerNumber; j++)
            {
                if (!map[i][j])
                {
                    flag = false;

                    break;
                }
            }

            if (flag)
            {
                answer += 1;
            }
        }

        return answer;
    }
}
