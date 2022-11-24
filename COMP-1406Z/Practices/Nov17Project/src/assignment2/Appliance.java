package assignment2;

public class Appliance extends Product{
    protected int wattage;
    protected String color;
    protected String brand;

    public Appliance(double price, int quantity, int wattage, String color, String brand){
        super(price, quantity);
        this.wattage = wattage;
        this.color = color;
        this.brand = brand;
    }
}
