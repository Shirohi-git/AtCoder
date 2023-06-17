import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A = sc.nextInt(), B = sc.nextInt();
        sc.close();

        int ans = Math.min(N * A, B);
        System.out.println(ans);
    }
}
