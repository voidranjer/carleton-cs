public class CustomerTestProgram {
    public static void main(String[] args) {
        Customer c;

        c = new Customer("Bob");
        c.name = "Bob";
        c.age = 27;
        c.money = 50;
        System.out.println(c.name);
        System.out.println(c.age);
        System.out.println(c.money);


        Customer anotherCustomer = new Customer("Lei");
        anotherCustomer.name = "Lei";
        anotherCustomer.age = 100;
        anotherCustomer.money = 1082318;
        System.out.println(anotherCustomer.name);
        System.out.println(anotherCustomer.age);
        System.out.println(anotherCustomer.money);
    }
}
