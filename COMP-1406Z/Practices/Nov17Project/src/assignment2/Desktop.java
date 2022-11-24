package assignment2;

public class Desktop extends Computer {
    private String profile;

    public Desktop(double price, int initQuantity, double cpuSpeed, int ram, boolean isSSD, int storage, String profile){
        super(price, initQuantity, cpuSpeed, ram, isSSD, storage);
        this.profile = profile;
    }

    public String toString(){
        String x = "Desktop PC with " + cpuSpeed + "ghz CPU, " +
                ram + "GB RAM, " + storage + "GB ";

        if(isSSD){
            x = x + "SSD drive";
        }else{
            x = x + "HDD drive";
        }

        return x;
    }
}
