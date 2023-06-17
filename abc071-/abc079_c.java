import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        int[] num = { N / 1000, N / 100 % 10, N / 10 % 10, N % 10 };
        int bit = 0;

        for (int i = 0; i < 8; i++) {
            int res = Arrays.stream(num).sum();
            for (int j = 0; j < 3; j++) {
                if ((i >> j & 1) == 0)
                    res -= 2 * num[j + 1];
            }
            if (res == 7) {
                bit = i;
                break;
            }
        }
        String ans = "=7";
        char[] ope = { '+', '+', '+' };
        for (int j = 0; j < 3; j++) {
            if ((bit >> j & 1) == 0)
                ope[j] = '-';
        }
        System.out.print("" + num[0] + ope[0] + num[1] + ope[1]);
        System.out.println("" + num[2] + ope[2] + num[3] + ans);
    }
}
