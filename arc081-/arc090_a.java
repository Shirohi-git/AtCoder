import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A1 = new int[N];
        int[] A2 = new int[N];
        for (int i = 0; i < N; i++)
            A1[i] = sc.nextInt();
        for (int i = 0; i < N; i++)
            A2[i] = sc.nextInt();
        sc.close();

        int ans = A1[0] + Arrays.stream(A2).sum();
        int res = ans;
        for (int i = 1; i < N; i++) {
            res += A1[i] - A2[i - 1];
            ans = Math.max(ans, res);
        }
        System.out.println(ans);
    }
}
