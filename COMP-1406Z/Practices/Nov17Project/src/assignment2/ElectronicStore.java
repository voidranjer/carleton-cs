package assignment2;

import java.util.Locale;
import java.util.Scanner;

public class ElectronicStore {
    private String name;
    private Product[] products;
    private double revenue; //how much money the store has collected
    private static final int MAX_PRODUCTS = 10;

    public ElectronicStore(String iName){
        name = iName;
        revenue = 0;
        products = new Product[MAX_PRODUCTS];
    }

    public String getName(){
        return name;
    }

    public double getRevenue(){
        return revenue;
    }

    public boolean addProduct(Product p){
        for(int i = 0; i < products.length; i++){
            if(products[i] == null){
                products[i] = p;
                return true;
            }
        }
        return false;
    }

    public boolean sellProducts(){
        printStock();
        Scanner in = new Scanner(System.in);
        System.out.print("Which index do you want to buy: ");
        int itemIndex = in.nextInt();
        System.out.print("How many? ");
        int amount = in.nextInt();
        return sellProducts(itemIndex, amount);
    }

    public boolean sellProducts(int unitIndex, int amount){
        //Check if unitIndex is valid (within range and a product there)
        if(unitIndex >= 0 && unitIndex < MAX_PRODUCTS && products[unitIndex] != null){
            //sell that product
            double saleAmount = products[unitIndex].sellUnits(amount);
            if(saleAmount >= 0){
                revenue += saleAmount;
                return true;
            }
        }
        return false;
    }

    public void printStock(){
        for(int i = 0; i < MAX_PRODUCTS; i++){
            if(products[i] != null) {
                System.out.println(i + ". " + products[i]);
            }
        }
    }

    public boolean searchStock(String query){
        for(int i = 0; i < products.length; i++){
            if(products[i] != null){
                if(products[i].toString().toLowerCase().contains(query.toLowerCase())) {
                    return true;
                }
            }
        }
        return false;
    }
}
