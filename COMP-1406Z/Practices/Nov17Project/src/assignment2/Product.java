package assignment2;

public abstract class Product {
    protected double price;
    protected int soldQuantity;
    protected int stockQuantity;

    public Product(double initPrice, int initStock){
        price = initPrice;
        stockQuantity = initStock;
        soldQuantity = 0;
    }

    public double sellUnits(int amount){
        if(stockQuantity >= amount){
            stockQuantity -= amount;
            soldQuantity += amount;
            return price * amount;
        }
        return -1;
    }
}
