import javafx.scene.control.Button;
import javafx.scene.layout.Pane;

public class DVDButtonPane extends Pane {
    private     Button  addButton, deleteButton, statsButton;

    public Button getAddButton() { return addButton; }
    public Button getDeleteButton() { return deleteButton; }
    public Button getStatsButton() { return statsButton; }

    public DVDButtonPane() {
        Pane innerPane = new Pane();

        // Create the buttons
        addButton = new Button("Add");
        addButton.setStyle("-fx-font: 12 arial; -fx-base: rgb(0,100,0); -fx-text-fill: rgb(255,255,255);");
        addButton.relocate(0, 0);
        addButton.setPrefSize(90,30);

        deleteButton = new Button("Delete");
        deleteButton.setStyle("-fx-font: 12 arial; -fx-base: rgb(200,0,0); -fx-text-fill: rgb(255,255,255);");
        deleteButton.relocate(95, 0);
        deleteButton.setPrefSize(90,30);

        statsButton = new Button("Stats");
        statsButton.setStyle("-fx-font: 12 arial;");
        statsButton.relocate(210, 0);
        statsButton.setPrefSize(90,30);

        // Add all three buttons to the pane
        innerPane.getChildren().addAll(addButton, deleteButton, statsButton);
//        getChildren().addAll(addButton, deleteButton, statsButton);

        getChildren().addAll(innerPane);//, titleLabel);
    }
}

