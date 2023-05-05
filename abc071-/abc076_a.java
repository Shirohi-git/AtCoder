import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt(), G = sc.nextInt();
        sc.close();

        int ans = G * 2 - R;
        System.out.println(ans);
    }
}
