public class Customer {
    String name;
    int age;
    float money;

    public Customer() {
        name = "Unknown";
        age = 0;
        money = 0.0f;
    }

    public Customer(String initName) {
        name = initName;
        age = 0;
        money = 0.0f;
    }

    public Customer(String initName, int initAge) {
        name = initName;
        age = initAge;
        money = 0.0f;
    }

    public Customer(String initName, int initAge, float initMoney) {
        name = initName;
        age = initAge;
        money = initMoney;
    }
}
