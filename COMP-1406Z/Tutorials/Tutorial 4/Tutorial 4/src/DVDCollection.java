public class DVDCollection {
    public static final int     MAX_DVDS = 100;

    private DVD[]   dvds;
    private int     dvdCount;

    public DVDCollection() { dvds = new DVD[MAX_DVDS]; }

    public DVD[] getDvds() { return dvds; }

    public DVD[] getDVDList() {
        DVD[] list = new DVD[dvdCount];
        for (int i=0; i<dvdCount; i++)
            list[i] = dvds[i];

        return list;
    }

    public String[] getDVDTitles() {
        String[] titles = new String[dvdCount];
        for (int i=0; i<dvdCount; i++)
            titles[i] = dvds[i].getTitle();

        return titles;
    }

    public Integer[] getDVDYears() {
        Integer[] years = new Integer[dvdCount];
        for (int i=0; i<dvdCount; i++)
            years[i] = dvds[i].getYear();

        return years;
    }

    public Integer[] getDVDLengths() {
        Integer[] lengths = new Integer[dvdCount];
        for (int i=0; i<dvdCount; i++)
            lengths[i] = dvds[i].getDuration();

        return lengths;
    }

    public int getDvdCount() { return dvdCount; }
    public String toString() { return ("DVD Collection of size " + dvdCount); }

    public void add(DVD aDvd) {
        if (dvdCount < MAX_DVDS)
            dvds[dvdCount++] = aDvd;
    }
    public boolean remove(String title) {
        for (int i=0; i<dvdCount; i++) {
            DVD d = dvds[i];
            if (dvds[i].getTitle().equals(title)) {
                dvds[i] = dvds[dvdCount-1];
                dvdCount--;
                return true;
            }
        }
        return false;
    }

    public static DVDCollection example1() {
        DVDCollection c = new DVDCollection();
        c.add(new DVD("If I Was a Student", 2007, 65));
        c.add(new DVD("Don't Eat Your Pencil !", 1984, 112));
        c.add(new DVD("The Exam", 2001, 180));
        c.add(new DVD("Tutorial Thoughts", 2003, 128));
        c.add(new DVD("Fried Monitors", 1999, 94));
        return c;
    }
}