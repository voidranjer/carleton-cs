public class Prize {
    private Point2D     location;
    private int 	    value;

    public Prize(Point2D loc, int val) {
        location = loc;
        value = val;
    }

    // The get/set methods
    public Point2D getLocation() { return location; }
    public int getValue() { return value; }

    public String toString() {
        return "Prize" + " at (" + (int)location.getX() + "," + (int)location.getY() + ") with value " + value;
    }
}