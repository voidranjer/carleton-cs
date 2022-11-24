public class Ball extends MovableObject implements Harmful{
    private boolean 	isBeingHeld;

    public Ball(Point2D loc) {
        super(0,0,loc);
        isBeingHeld = false;
    }

    // The get/set methods
    public boolean isBeingHeld() { return isBeingHeld; }
    public void setIsBeingHeld(boolean newHoldStatus) { isBeingHeld = newHoldStatus; }

    public String toString() {
        return "Ball" + " at (" + (int)location.getX() + "," + (int)location.getY() + ") facing " + direction +
                " degrees going " + speed + " pixels per second";
    }

    @Override
    public void draw() {
        System.out.println("Ball" + " at (" + (int)location.getX() + "," + (int)location.getY() + ") facing " + direction +
                " degrees going " + speed + " pixels per second");
    }

    public void update() {
        super.update();
        if (speed > 0) speed--;
    }

    @Override
    public int getDamageAmount() {
        return -200;
    }
}