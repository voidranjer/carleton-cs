import java.util.Scanner;

public class Football {
  public static void main(String args[]) {
    final int MAX_LENGTH = 7;
    Scanner input = new Scanner(System.in);

    String raw = input.nextLine();
    int rawLength = raw.length();

    int currentIndex = 0;
    int streak = 1;
    char prevChar = '2';
    char currentChar = '2';

    boolean isDangerous = false;

    while (currentIndex < rawLength) {
      currentChar = raw.charAt(currentIndex);

      if (currentChar == prevChar) {
        streak++;
      } else {
        streak = 1;
      }

      // System.out.println(streak + " " + currentChar);

      if (streak >= MAX_LENGTH) {
        isDangerous = true;
      }

      prevChar = currentChar;
      currentIndex++;
    }

    System.out.println(isDangerous ? "YES" : "NO");

  }
}