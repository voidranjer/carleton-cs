package assignment2;

public class ToasterOven extends Appliance {
    private int width;
    private boolean convection;

    public ToasterOven(double price, int quantity, int wattage, String color, String brand,
                   int width, boolean convection){
        super(price, quantity, wattage, color, brand);
        this.width = width;
        this.convection = convection;
    }

    public String toString(){
        String result = width + " inch toaster ";
        if(convection){
            result += "with convection ";
        }

        result += "(" + color + ")";
        return result;
    }
}
