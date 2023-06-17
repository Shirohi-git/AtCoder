import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();
        int L = 87;

        long[] ans = new long[L];
        ans[0] = 2;
        ans[1] = 1;
        for (int i = 2; i < L; i++) {
            ans[i] = ans[i - 1] + ans[i - 2];
        }
        System.out.println(ans[N]);
    }
}
