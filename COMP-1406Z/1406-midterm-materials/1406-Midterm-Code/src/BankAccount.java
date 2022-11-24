public abstract class BankAccount {
    private String owner;
    private Bank institution;
    private double balance;
    private int accountNumber;
    protected final double MONTHLY_FEE = 1.00;

    /*
    Constructor for BankAccount
    Accepts an owner name (String), institution (Bank) and account number (int)
     */
    public BankAccount(String initOwner, Bank initInstitution, int initNumber) {
        balance = 0.0;
        accountNumber = initNumber;
        institution = initInstitution;
        owner = initOwner;
    }

    protected void setBalance(double newBalance) {
        if (newBalance >= 0) {
            balance = newBalance;
        }
    }

    public void setInstitution(Bank newInst){
        institution = newInst;
    }

    public double getBalance() {
        return balance;
    }

    public String getOwner() {
        return owner;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public Bank getInstitution() {
        return institution;
    }

    //Withdraw the given amount if possible
    //Returns true to indicate success and false otherwise
    public boolean withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }

    //Deposits the given amount if it is greater than 0
    //Returns true to indicate success and false otherwise
    public boolean deposit(double amount) {
        if (amount >= 0) {
            balance += amount;
            return true;
        }
        return false;
    }

    //Charges the monthly fee for the account
    public void monthlyUpkeep() {
        withdraw(MONTHLY_FEE);
    }

    public String toString() {
        return owner + "'s BANK account #" + accountNumber + " at " + institution + " with balance $" + balance;
    }
}