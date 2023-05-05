import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), K = sc.nextInt();
        sc.close();

        int num = 1;
        for (int i = 0; i < N; i++) {
            if (num * 2 < num + K)
                num *= 2;
            else
                num += K;
        }
        System.out.println(num);
    }
}
