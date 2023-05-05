import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt(), W = sc.nextInt();
        char[][] S = new char[H][W];
        for (int i = 0; i < H; i++) {
            S[i] = sc.next().toCharArray();
        }
        sc.close();

        int[][] near = new int[9][2];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                near[i * 3 + j][0] = i-1;
                near[i * 3 + j][1] = j-1;
            }
        }

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (S[i][j] == '#') {
                    System.out.print(S[i][j]);
                    continue;
                }
                int cnt = 0;
                for (int[] xy : near) {
                    int x = xy[0], y = xy[1];
                    if (i + x < 0 || H <= i + x)
                        continue;
                    if (j + y < 0 || W <= j + y)
                        continue;
                    if (S[i + x][j + y] == '#')
                        cnt++;
                }
                System.out.print(cnt);
            }
            System.out.println();
        }
    }
}
