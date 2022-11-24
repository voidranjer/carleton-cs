public class Trap {
    private Point2D     location;

    public Trap(Point2D loc) {
        location = loc;
    }

    // The get method
    public Point2D getLocation() { return location; }

    public String toString() {
        return "Trap" + " at (" + (int)location.getX() + "," + (int)location.getY() + ")";
    }
}