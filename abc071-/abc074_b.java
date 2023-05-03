import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int X[] = new int[N];
        for (int i = 0; i < N; i++) {
            X[i] = sc.nextInt();
        }
        sc.close();

        int ans = 0;
        for (int xi : X) {
            ans += Math.min(xi, (K - xi));
        }
        ans *= 2;
        System.out.println(ans);
    }
}
