package assignment2;

public class Laptop extends Computer{
    int screenSize;

    public Laptop(double initPrice, int initStock, double cpuSpeed, int ram, boolean isSSD, int storage, int screenSize){
        super(initPrice, initStock, cpuSpeed, ram, isSSD, storage);
        this.screenSize = screenSize;
    }

    public String toString(){
        String x = screenSize + "\"Laptop PC with " + cpuSpeed + "ghz CPU, " +
                ram + "GB RAM, " + storage + "GB ";

        if(isSSD){
            x = x + "SSD drive";
        }else{
            x = x + "HDD drive";
        }

        return x;
    }
}
