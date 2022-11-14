public class Customer {
    String name;
    int age;
    float money;
    boolean admitted;

    public Customer() {
        name = "Unknown";
        age = 0;
        money = 0.0f;
        admitted = false;
    }

    public Customer(String initName) {
        name = initName;
        age = 0;
        money = 0.0f;
        admitted = false;
    }

    public Customer(String initName, int initAge) {
        name = initName;
        age = initAge;
        money = 0.0f;
        admitted = false;
    }

    public Customer(String initName, int initAge, float initMoney) {
        name = initName;
        age = initAge;
        money = initMoney;
        admitted = false;
    }

    public float computeFee() {
        if (age <= 3) return 0.0f;
        if (age >= 65) return 12.75f / 2;
        if (age >= 4 && age <= 17) return 8.5f;
        return 12.75f;

    }

    public boolean spend(float amount) {
        if (amount < 0) return false;
        if (amount > money) return false;
        money = money - amount;
        return true;
    }

    public boolean hasMoreMoneyThan(Customer c) {
        if (money > c.money) return true;
        return false;
    }

    public void payAdmission() {
        if (spend(computeFee())) admitted = true;
        else admitted = false;
    }

    public String toString() {
        return String.format("Customer %s: a %d year old with $%,.2f who has%s been admitted", name, age, money, admitted ? "" : " not");
    }
}
