public class Trap extends StationaryObject implements Harmful {

    public Trap(Point2D loc) {
        super(loc);
    }

    // The get method
    public Point2D getLocation() { return location; }

    public String toString() {
        return "Trap" + " at (" + (int)location.getX() + "," + (int)location.getY() + ")";
    }

    @Override
    public int getDamageAmount() {
        return -50;
    }
}