import java.util.Scanner;

public class TaxProgram {
    public static void main(String[] args) {
        double income, fedTax, provTax;
        int dependents;

        Scanner input = new Scanner(System.in);

        System.out.print("Please enter your taxable income: ");
        income = input.nextDouble();

        System.out.print("Please enter your number of dependents: ");
        dependents = input.nextInt();
        System.out.println();

        fedTax = 0.0;
        provTax = 0.0;

        // Federal Tax
        if (income <= 29590) {
            fedTax = income * 0.17;
        } else if (income <= 59179.99) {
            fedTax = 29590 * 0.17 + (income - 29590) * 0.26;
        } else {
            fedTax = (29590 * 0.17) + (29590 * 0.26) + (income - 59180) * 0.29;
        }

        // Provincial Tax
        provTax = fedTax * 0.425;
        double deductions = 160.5 + (328 * dependents);
        if (provTax > deductions) {
            provTax = provTax - deductions;
        } else {
            provTax = 0.0;
        }

        String fString = "%-18s$%,9.2f\n";

        System.out.println("Here is your tax breakdown:\n");
        System.out.printf(fString, "Income", income);
        System.out.printf("%-26s%2d\n", "Dependents", dependents);
        System.out.println("----------------------------");
        System.out.printf(fString, "Federal Tax", fedTax);
        System.out.printf(fString, "Provincial Tax", provTax);
        System.out.println("============================");
        System.out.printf(fString, "Total Tax", fedTax + provTax);
    }
}
