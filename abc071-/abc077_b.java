import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        int ans = 0;
        for (int i = 0; i*i <= N; i++) {
            ans = i * i;
        }
        System.out.println(ans);
    }
}
