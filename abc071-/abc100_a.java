import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        sc.close();

        String ans = "Yay!";
        if (A > 8 || B > 8) {
            ans = ":(";
        }
        System.out.println(ans);
    }
}