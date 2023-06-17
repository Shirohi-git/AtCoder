import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        sc.close();

        int fx = 0, x = X;
        while (x > 0) {
            fx += x % 10;
            x /= 10;
        }

        String ans = "No";
        if (X % fx == 0)
            ans = "Yes";
        System.out.println(ans);
    }
}
