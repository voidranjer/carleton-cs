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
                int index = view.getTitleList().getSelectionModel().getSelectedIndex();

                // Nothing is selected
                if (index == -1) {
                    javax.swing.JOptionPane.showMessageDialog(null, "Please make a selection first!");
                    return;
                }

                model.remove(index);
                view.update(model, 0);
            }
        });


        view.getTitleList().setOnMousePressed(new EventHandler<MouseEvent>() {
            public void handle(MouseEvent mouseEvent) {
                view.update(model, view.getTitleList().getSelectionModel().getSelectedIndex());
            }
        });

    }

    public static void main(String[] args) {
        launch(args);
    }
}