public class CustomerConstructorTestProgram {
    public static void main(String args[]) {
        Customer c1, c2, c3, c4;
        c1 = new Customer("Bob", 17);
        c2 = new Customer("Dottie", 3, 10);
        c3 = new Customer("Jane");
        c4 = new Customer();
        
        System.out.println("Bob looks like this: " + c1.name +
                ", " + c1.age + ", " + c1.money);
        System.out.println("Dottie looks like this: " + c2.name +
                ", " + c2.age + ", " + c2.money);
        System.out.println("Jane looks like this: " + c3.name +
                ", " + c3.age + ", " + c3.money);
        System.out.println("Customer 4 looks like this: " + c4.name +
                ", " + c4.age + ", " + c4.money);
    }
}