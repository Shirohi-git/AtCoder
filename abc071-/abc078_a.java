import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String X = sc.next(), Y = sc.next();
        sc.close();

        if (X.compareTo(Y) == 0)
            System.out.println("=");
        if (X.compareTo(Y) < 0)
            System.out.println("<");
        if (X.compareTo(Y) > 0)
            System.out.println(">");
    }
}
