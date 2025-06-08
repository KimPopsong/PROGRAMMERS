import java.util.*;

class Solution {
    static Set<String> canDraw = new HashSet<>();  // 교점의 모든 좌표 저장

    public String[] solution(int[][] line)
    {
        String[] answer;

        for (int i = 0; i < line.length - 1; i++)  // 교점의 좌표 구하기
        {
            long A = line[i][0];
            long B = line[i][1];
            long E = line[i][2];

            for (int j = i + 1; j < line.length; j++)
            {
                long C = line[j][0];
                long D = line[j][1];
                long F = line[j][2];

                long x = 0, y = 0;

                if (A * D == B * C)  // 평행하거나 일치한다면
                {
                    continue;
                }

                if ((B * F - E * D) % (A * D - B * C) == 0)  // x 좌표가 정수라면
                {
                    x = (B * F - E * D) / (A * D - B * C);
                }

                else
                {
                    continue;
                }

                if ((E * C - A * F) % (A * D - B * C) == 0)  // y 좌표가 정수라면
                {
                    y = (E * C - A * F) / (A * D - B * C);
                }

                else
                {
                    continue;
                }

                canDraw.add(x + " " + y);
            }
        }

        long minX = Long.MAX_VALUE;
        long minY = Long.MAX_VALUE;
        long maxX = Long.MIN_VALUE;
        long maxY = Long.MIN_VALUE;

        for (String s : canDraw)
        {
            String[] temp = s.split(" ");

            long x = Long.parseLong(temp[0]);
            long y = Long.parseLong(temp[1]);

            if (x < minX)
            {
                minX = x;
            }

            if (x > maxX)
            {
                maxX = x;
            }

            if (y < minY)
            {
                minY = y;
            }

            if (y > maxY)
            {
                maxY = y;
            }
        }

        char[][] draw = new char[(int) (maxY - minY) + 1][(int) (maxX - minX) + 1];
        answer = new String[(int) (maxY - minY) + 1];

        for (String s : canDraw)
        {
            String[] temp = s.split(" ");

            long x = Long.parseLong(temp[0]);
            long y = Long.parseLong(temp[1]);

            x -= minX;
            y -= minY;

            draw[(int) y][(int) x] = '*';
        }

        for (int i = 0; i < draw.length; i++)
        {
            char[] l = draw[i];
            String temp = "";

            for (char ll : l)
            {
                if (ll == '*')
                {
                    temp += '*';
                }

                else
                {
                    temp += '.';
                }
            }

            answer[draw.length - i - 1] = temp;
        }

        return answer;
    }
}
