public class ChequingAccount extends BankAccount {
    public ChequingAccount(String initOwner, Bank initInstitution, int initNumber) {
        super(initOwner, initInstitution, initNumber);
    }

    public boolean writeCheque(double amount) {
        return withdraw(amount);
    }

    public String toString() {
        return getOwner() + "'s CHEQUING account #" + getAccountNumber() + " at " + getInstitution() + " with balance $" + getBalance();
    }
}