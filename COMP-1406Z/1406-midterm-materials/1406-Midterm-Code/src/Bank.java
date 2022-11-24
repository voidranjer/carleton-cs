public class Bank {
    private String name;
    private BankAccount[] accounts;
    private final int DEFAULT_NUM_ACCOUNTS = 10;

    public Bank(String name) {
        this.name = name;
        accounts = new BankAccount[DEFAULT_NUM_ACCOUNTS];
    }

    // Custom number of accounts
    public Bank(String name, int numAccounts) {
        this.name = name;
        accounts = new BankAccount[numAccounts];
    }

    // Count the current number of accounts in the bank
    public int countAccounts() {
        int count = 0;
        for (int i = 0; i < accounts.length; i++) {
            if (accounts[i] != null) {
                count++;
            }
        }
        return count;
    }

    public String toString() {
        return String.format("%s has %d accounts", name, countAccounts());
    }

    public boolean addAccount(BankAccount account) {
        for (int i = 0; i < accounts.length; i++) {

            // If the account is already in the array, return false (early return stops the function)
            if (accounts[i] != null && (accounts[i].getAccountNumber() == account.getAccountNumber())) return false;

            // Otherwise, attempt to add the account to the end of the array
            if (accounts[i] == null) {
                accounts[i] = account;
                account.setInstitution(this);
                return true;
            }
        }

        // Nothing worked (array is full), so return false
        return false;
    }

    public double getLargestBalance() {
        double largest = 0;
        for (BankAccount account : accounts) {
            if (account != null && account.getBalance() > largest) {
                largest = account.getBalance();
            }
        }
        return largest;
    }

    public void performMonthlyUpkeep() {
        for (BankAccount account : accounts) {
            if (account != null) account.monthlyUpkeep();
        }
    }

    public boolean transfer(int source, int destination, double amount) {
        BankAccount sourceAccount = accounts[source];
        BankAccount destinationAccount = accounts[destination];

        // Not enough money in the source account
        if (sourceAccount.getBalance() < amount) return false;

        // Amount given is negative
        if (amount < 0) return false;

        // Source and destination indices are identical
        if (source == destination) return false;
        if (sourceAccount == destinationAccount) return false;

        // Either of the specified account indices are not valid
        if (sourceAccount == null || destinationAccount == null) return false;

        // Perform transfer
        sourceAccount.withdraw(amount);
        destinationAccount.deposit(amount);
        return true;
    }

    public static void main(String[] args) {

        // Create a new bank object
        Bank bank = new Bank("TD");

        // Create accounts
        ChequingAccount c1 = new ChequingAccount("Bob", bank, 1);
        ChequingAccount c2 = new ChequingAccount("Alice", bank, 2);
        SavingsAccount s1 = new SavingsAccount("Bob", bank, 3);
        SavingsAccount s2 = new SavingsAccount("Alice", bank, 4);

        // Add accounts to bank
        boolean addSucceeded = bank.addAccount(c1) && bank.addAccount(c2) && bank.addAccount(s1) && bank.addAccount(s2);
        System.out.println("All accounts added successfully: " + addSucceeded);

        // Print bank information
        System.out.println(bank.toString());

        // Add balance to accounts
        boolean depositSucceeded = c1.deposit(100) && c2.deposit(200) && s1.deposit(300) && s2.deposit(400);
        System.out.println("All deposits succeeded: " + depositSucceeded);

        // Perform monthly upkeep (for a year)
        for (int i = 0; i < 12; i++) {
            bank.performMonthlyUpkeep();
        }

        // Print largest balance
        System.out.println("Largest balance: " + bank.getLargestBalance());

        // Transfer money
        boolean transferSucceeded = bank.transfer(0, 1, 50);
        System.out.println("Transfer succeeded: " + transferSucceeded);
    }
}