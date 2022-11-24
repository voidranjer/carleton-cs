package assignment2;

public class Computer extends Product{
    protected double cpuSpeed;
    protected int ram;
    protected boolean isSSD;
    protected int storage;

    public Computer(double price, int quantity, double cpuSpeed, int ram, boolean ssd, int
            storage){
        super(price, quantity);
        this.cpuSpeed = cpuSpeed;
        this.ram = ram;
        this.isSSD = ssd;
        this.storage = storage;
    }
}
