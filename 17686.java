import java.util.ArrayList;
import java.util.Collections;

class Solution {

    String[] answer;

    public String[] solution(String[] files) {
        answer = new String[files.length];
        ArrayList<File> fileList = new ArrayList<>();

        for (String f : files) {
            fileList.add(new File(f));
        }

        Collections.sort(fileList);

        int i = 0;
        for (File f : fileList) {
            answer[i++] = f.original;
        }

        return answer;
    }

    static class File implements Comparable<File> {

        String original, head;
        int number;

        File(String file) {
            original = file;

            int i = 0;

            while (!Character.isDigit(file.charAt(i))) {
                i += 1;
            }

            head = file.substring(0, i);

            int j = i;
            while (j < file.length() && Character.isDigit(file.charAt(j))) {
                j += 1;
            }

            number = Integer.parseInt(file.substring(i, j));
        }

        @Override
        public int compareTo(File f) {
            int headCompare = this.head.compareToIgnoreCase(f.head);

            if (headCompare == 0) {
                return Integer.compare(this.number, f.number);
            } else {
                return headCompare;
            }
        }
    }
}
