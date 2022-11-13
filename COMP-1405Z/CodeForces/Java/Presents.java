import java.util.Scanner;

public class Presents {
  public static void main(String args[]) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();

    int[] numbers = new int[n];

    for (int i = 0; i < n; i++) {
      numbers[input.nextInt() - 1] = i;
    }

    for (int i = 0; i < n; i++) {
      System.out.print(numbers[i] + 1 + " ");
    }
  }
}
