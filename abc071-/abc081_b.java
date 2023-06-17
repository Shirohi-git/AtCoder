import java.util.*;

class Main {
    static int gcd(int a, int b) {
        int tmp = a % b;
        while (tmp != 0) {
            a = b;
            b = tmp;
            tmp = a % b;
        }
        return b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++)
            A[i] = sc.nextInt();
        sc.close();

        int res = A[0];
        for (int ai : A)
            res = gcd(ai, res);

        int ans = 0;
        while (res % 2 == 0) {
            ans += 1;
            res /= 2;
        }
        System.out.println(ans);
    }
}
