import java.util.Scanner;

public class TheatreSquare {
  public static void main(String args[]) {
    Scanner input = new Scanner(System.in);
    double m, n, a;

    m = input.nextDouble();
    n = input.nextDouble();
    a = input.nextDouble();

    double x = Math.ceil(m / a);
    double y = Math.ceil(n / a);

    if (m < a) {
      x = 1;
    }

    if (n < a) {
      y = 1;
    }

    double result = (x * y);

    System.out.println((long) result);

  }
}