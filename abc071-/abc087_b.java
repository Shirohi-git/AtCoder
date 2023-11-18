import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int X = sc.nextInt();
        sc.close();

        int ans = 0;
        for (int i = 0; i <= A; i++) {
            for (int j = 0; j <= B; j++) {
                for (int k = 0; k <= C; k++) {
                    int p = 500 * i + 100 * j + 50 * k;
                    if (p == X)
                        ans++;
                }
            }
        }
        System.out.println(ans);
    }
}
