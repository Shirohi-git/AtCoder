import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        int ans = 0;
        while (N > 0) {
            ans += N % 10;
            N /= 10;
        }
        System.out.println(ans);
    }
}
