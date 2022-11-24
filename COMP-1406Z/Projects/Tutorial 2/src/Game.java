public class Game {
    public static final int     MAX_GAME_OBJECTS = 1000;

    GameObject[]        gameObjects;
    int             objectCount;

    public Game() {
        gameObjects = new GameObject[MAX_GAME_OBJECTS];
        objectCount = 0;
    }

    public void add(GameObject obj) {
        if (objectCount < MAX_GAME_OBJECTS)
            gameObjects[objectCount++] = obj;
    }

    // The get methods
    public GameObject[] getGameObjects() { return gameObjects; }
    public int getObjectCount() { return objectCount; }

    public String toString() {
        return "Game with " + objectCount + " objects";
    }

    public void displayObjects() {
        for (int i=0; i<objectCount; i++)
            System.out.println(gameObjects[i]);
    }

    public void updateObjects() {
        for (int i=0; i<objectCount; i++)
            gameObjects[i].update();
    }

    // Return an array of all Harmful objects in the game
    public Harmful[] harmfulObjects() {
        // First find out how many objects are Harmful
        int count = 0;
        for (GameObject g: gameObjects)
            if (g instanceof Harmful)
                count++;

        // Now create the array and fill it up
        Harmful[] bad = new Harmful[count];
        count = 0;
        for (GameObject g: gameObjects)
            if (g instanceof Harmful)
                bad[count++] = (Harmful)g;
        return bad;
    }

    public int assessDanger() {
        int sumDamage = 0;
        Harmful[] dangerousStuff = harmfulObjects();
        for (Harmful h: dangerousStuff)
            sumDamage += h.getDamageAmount();
        return sumDamage;
    }
}