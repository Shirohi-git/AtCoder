import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A = sc.nextInt();
        sc.close();

        int ans = N * N - A;
        System.out.println(ans);
    }
}