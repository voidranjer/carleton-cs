public class Ball {
    private Point2D     location;
    private int			direction;
    private int 		speed;
    private boolean 	isBeingHeld;

    public Ball(Point2D loc) {
        location = loc;
        direction = 0;
        speed = 0;
        isBeingHeld = false;
    }

    // The get/set methods
    public Point2D getLocation() { return location; }
    public int getDirection() { return direction; }
    public int getSpeed() { return speed; }
    public boolean isBeingHeld() { return isBeingHeld; }
    public void setLocation(Point2D newLocation) { location = newLocation; }
    public void setDirection(int newDirection) { direction = newDirection; }
    public void setSpeed(int newSpeed) { speed = newSpeed; }
    public void setIsBeingHeld(boolean newHoldStatus) { isBeingHeld = newHoldStatus; }

    public String toString() {
        return "Ball" + " at (" + (int)location.getX() + "," + (int)location.getY() + ") facing " + direction +
                " degrees going " + speed + " pixels per second";
    }
}