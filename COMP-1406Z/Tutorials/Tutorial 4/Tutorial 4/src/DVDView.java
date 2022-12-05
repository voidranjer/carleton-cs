import javafx.scene.control.ListView;

public interface DVDView {
    // Cause view to update its appearance based on given model & selected DVD

    public void update(DVDCollection model, int selectedDVD);
    public ListView<Integer> getYearList();
    public ListView<Integer> getLengthList();
}
