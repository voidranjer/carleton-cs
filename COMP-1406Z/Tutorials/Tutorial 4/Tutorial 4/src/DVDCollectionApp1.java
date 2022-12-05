import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.event.*;

import java.util.Scanner;

public class DVDCollectionApp1  extends Application {
    private DVDCollection model;

    public DVDCollectionApp1() { this.model = DVDCollection.example1(); }

    public void start(Stage primaryStage) {
        Pane  aPane = new Pane();

        // Create the view
        DVDCollectionAppView1 view = new DVDCollectionAppView1();
//        DVDCollectionAppView2 view = new DVDCollectionAppView2();
        aPane.getChildren().add(view);

        primaryStage.setTitle("My DVD Collection");
        primaryStage.setResizable(false);
        primaryStage.setScene(new Scene(aPane));
        primaryStage.show();
        view.update(model, 0);

        // Event handlers
        view.getButtonPane().getAddButton().setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent actionEvent) {
                String title;
                int year, duration;

                try {
                    title = javax.swing.JOptionPane.showInputDialog("Enter DVD title: ");
                    if (title.strip().length() == 0) throw new Exception();
                    year = Integer.parseInt(javax.swing.JOptionPane.showInputDialog("Enter year: "));
                    duration = Integer.parseInt(javax.swing.JOptionPane.showInputDialog("Enter duration (in minutes): "));
                } catch (Exception e) {
                    javax.swing.JOptionPane.showMessageDialog(null, "Invalid input, please try again");
                    return; // Early return due to error (stops the rest of the code from running)
                }

                DVD dvd = new DVD(title, year, duration);
                model.add(dvd);
                view.update(model, 0);
            }
        });

        view.getButtonPane().getDeleteButton().setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent actionEvent) {
                // NOTE: This system will break down if there are multiple DVDs with the same title in the list.
                // It will delete the first one it finds. In this case, the DVDs are sorted alphabetically by title.
                // However, since this is not mentioned in the instructions, and the remove() method in the model was already defined by the prof, I will assume that this is to simplify things and not overcomplicate the code, so I will leave it as it is.
                Object selectedDVD = view.getTitleList().getSelectionModel().getSelectedItem();

                // Nothing is selected
                if (selectedDVD == null) {
                    javax.swing.JOptionPane.showMessageDialog(null, "Please make a selection first!");
                    return;
                }

                // Depending on View1 or View2, "selectedDVD" could be type of either "DVD" or "String"
                String title = selectedDVD.toString();
                if (selectedDVD instanceof DVD) title = ((DVD) selectedDVD).getTitle();

                model.remove(title);
                view.update(model, 0);
            }
        });

        if (view.getYearList() != null) {
            view.getTitleList().setOnMousePressed(new EventHandler<MouseEvent>() {
                public void handle(MouseEvent mouseEvent) {
                    int index = view.getTitleList().getSelectionModel().getSelectedIndex();
                    view.getYearList().getSelectionModel().selectIndices(index);
                    view.getLengthList().getSelectionModel().selectIndices(index);
                }
            });
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}