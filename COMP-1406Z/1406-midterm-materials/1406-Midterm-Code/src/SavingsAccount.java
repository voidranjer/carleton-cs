public class SavingsAccount extends BankAccount {
    //The interest rate that should be added to the account each month
    private static final double INTEREST_RATE = 0.01;

    //The fee to charge for each withdraw
    private static final double WITHDRAW_FEE = 1.0;

    public SavingsAccount(String initOwner, Bank initInstitution, int initNumber) {
        super(initOwner, initInstitution, initNumber);
    }

    public boolean withdraw(double amount) {
        return super.withdraw(amount + WITHDRAW_FEE);
    }

    public void monthlyUpkeep() {
        setBalance(getBalance() + (getBalance() * INTEREST_RATE));
    }

    public String toString() {
        return getOwner() + "'s SAVINGS account #" + getAccountNumber() + " at " + getInstitution() + " with balance $" + getBalance();
    }
}