import java.util.ArrayDeque;

class Solution {

    static int leftBox, rowSize, colSize;
    static char[][] warehouse;

    static int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};

    public int solution(String[] storage, String[] requests) {
        rowSize = storage.length;
        colSize = storage[0].length();
        leftBox = rowSize * colSize;

        warehouse = new char[rowSize][colSize];

        for (int r = 0; r < rowSize; r++) {
            for (int c = 0; c < colSize; c++) {
                warehouse[r][c] = storage[r].charAt(c);
            }
        }

        ArrayDeque<Point> bfs = new ArrayDeque<>();

        for (int c = 0; c < colSize; c++) {
            bfs.add(new Point(0, c));
            bfs.add(new Point(rowSize - 1, c));
        }

        for (int r = 1; r < rowSize - 1; r++) {
            bfs.add(new Point(r, 0));
            bfs.add(new Point(r, colSize - 1));
        }

        for (String request : requests) {
            char todo = request.charAt(0);

            if (request.length() == 1) {  // 가져올 수 있는 짐만 꺼내기
                ArrayDeque<Point> newBfs = new ArrayDeque<>(bfs);
                bfs.clear();

                while (!newBfs.isEmpty()) {
                    Point p = newBfs.removeFirst();

                    char box = warehouse[p.r][p.c];

                    if (box == todo) {  // 옮겨야 하는 짐
                        leftBox -= 1;
                        warehouse[p.r][p.c] = '0';
                    }

                    bfs.addLast(p);
                }
            } else {  // 모든 짐 꺼내기
                for (int r = 0; r < rowSize; r++) {
                    for (int c = 0; c < colSize; c++) {
                        if (warehouse[r][c] == todo) {
                            warehouse[r][c] = '0';

                            leftBox -= 1;
                        }
                    }
                }
            }

            // BFS에 새로 생긴 경로를 추가
            ArrayDeque<Point> newBfs = new ArrayDeque<>(bfs);
            bfs.clear();

            while (!newBfs.isEmpty()) {
                Point p = newBfs.removeFirst();

                if (warehouse[p.r][p.c] == '0') {
                    warehouse[p.r][p.c] = '-';

                    for (int d = 0; d < 4; d++) {
                        int rr = p.r + dr[d];
                        int cc = p.c + dc[d];

                        if (0 <= rr && rr < rowSize && 0 <= cc && cc < colSize) {
                            if (warehouse[rr][cc] == '-') {
                                continue;
                            } else if (warehouse[rr][cc] == '0') {
                                newBfs.addLast(new Point(rr, cc));
                            } else {
                                bfs.addLast(new Point(rr, cc));
                            }
                        }
                    }
                } else if (warehouse[p.r][p.c] == '-') {
                    continue;
                } else {
                    bfs.addLast(p);
                }
            }
        }

        return leftBox;
    }

    static class Point {

        int r, c;

        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}
