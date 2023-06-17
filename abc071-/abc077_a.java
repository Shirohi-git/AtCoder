import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String C1 = sc.next();
        String C2 = sc.next();
        sc.close();

        StringBuilder tmp1 = new StringBuilder(C1);
        String c1 = tmp1.reverse().toString();
        StringBuilder tmp2 = new StringBuilder(C2);
        String c2 = tmp2.reverse().toString();

        String ans = "NO";
        if (C1.equals(c2) && C2.equals(c1))
            ans = "YES";
        System.out.println(ans);
    }
}
