import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        sc.close();

        int ans = A;
        if (A == C)
            ans = B;
        if (A == B)
            ans = C;
        System.out.println(ans);
    }
}
