import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String N = sc.next();
        sc.close();

        char[] n = N.toCharArray();
        String ans = "No";
        if (n[0] == n[1] && n[1] == n[2])
            ans = "Yes";
        if (n[1] == n[2] && n[2] == n[3])
            ans = "Yes";
        System.out.println(ans);
    }
}
