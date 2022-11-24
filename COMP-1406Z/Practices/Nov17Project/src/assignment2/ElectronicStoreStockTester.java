package assignment2;

public class ElectronicStoreStockTester{
  public static void main(String[] args){

    ElectronicStore store1 = ElectronicStoreCreator.createStore1();
    ElectronicStore store2 = ElectronicStoreCreator.createStore2();
    ElectronicStore store3 = ElectronicStoreCreator.createStore3();
    
    System.out.println(store1.getName() + "'s Stock Is:");
    store1.printStock();
    System.out.println();
    System.out.println(store2.getName() + "'s Stock Is:");
    store2.printStock();
    System.out.println();
    System.out.println(store3.getName() + "'s Stock Is:");
    store3.printStock();

  }
}