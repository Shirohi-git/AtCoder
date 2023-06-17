import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long X = sc.nextInt();
        long Y = sc.nextInt();
        long Z = sc.nextInt();
        sc.close();

        long ans = 0;
        for (long i = 1; i <= X; i++) {
            if (Y * i + Z * (i + 1) <= X)
                ans = i;
        }
        System.out.println(ans);
    }
}
