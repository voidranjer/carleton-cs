package assignment2;

public class Fridge extends Appliance{
    double cubicFeet;
    boolean hasFreezer;

    public Fridge(double price, int quantity, int wattage, String color, String brand,
                  double cubicFeet, boolean freezer){
        super(price, quantity, wattage, color, brand);
        this.cubicFeet = cubicFeet;
        this.hasFreezer = freezer;
    }

    public String toString(){
        String result = cubicFeet + " cubic foot Fridge ";
        if(hasFreezer){
            result += "with Freezer ";
        }
        return result + "(" + color + ")";
    }
}
