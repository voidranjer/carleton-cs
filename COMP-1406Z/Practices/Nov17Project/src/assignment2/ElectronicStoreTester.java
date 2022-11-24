package assignment2;
import java.util.Scanner;

public class ElectronicStoreTester {
    public static void main(String[] args) {
        ElectronicStore store = new ElectronicStore("BestBuy");
        store.printStock();

        Scanner in = new Scanner(System.in);
        System.out.print("Enter a term to search for: ");
        String q = in.nextLine();

        while(!q.toLowerCase().equals("quit")){
            if(store.searchStock(q)){
                System.out.println("A matching item is in stock");
            }else{
                System.out.println("Go look at FutureShop");
            }

            System.out.print("Enter a term to search for: ");
            q = in.nextLine();
        }
    }
}
