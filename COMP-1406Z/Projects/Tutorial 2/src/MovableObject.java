public abstract class MovableObject extends  GameObject{
    protected int			direction;
    protected int 		speed;

    public MovableObject(int d, int s, Point2D loc) {
        super(loc);
        direction = d;
        speed = s;
    }

    public Point2D getLocation() { return location; }
    public int getDirection() { return direction; }
    public int getSpeed() { return speed; }
    public void setLocation(Point2D newLocation) { location = newLocation; }
    public void setDirection(int newDirection) { direction = newDirection; }
    public void setSpeed(int newSpeed) { speed = newSpeed; }

    public void moveForward() {
        if (speed > 0){
            location = location.add((int)
                    (Math.cos(Math.toRadians(direction)) * speed), (int)
                    (Math.sin(Math.toRadians(direction)) * speed));
        }}

    public void update() {
        moveForward();
        draw();
    }

    public abstract void draw();
}
