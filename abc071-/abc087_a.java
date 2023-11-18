import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        sc.close();


        int ans = X - A;
        ans %= B;
        System.out.println(ans);
    }
}
