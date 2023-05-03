import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int D = sc.nextInt();
        int N = sc.nextInt();
        int C = 100;
        sc.close();

        int ans = (int) Math.pow(C, D);
        if (N == 100) {
            N++;
        }
        ans *= N;
        System.out.println(ans);
    }
}