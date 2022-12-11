public class BinaryTreeTestProgram {
    public static void main(String[] args) {
        BinaryTree 	root;

        root = new BinaryTree("A",
                new BinaryTree("B",
                        new BinaryTree("C",
                                new BinaryTree("D"),
                                new BinaryTree("E",
                                        new BinaryTree("F",
                                                new BinaryTree("G"),
                                                new BinaryTree("I")),
                                        new BinaryTree("H"))),
                        new BinaryTree("J",
                                new BinaryTree("K",
                                        new BinaryTree(),
                                        new BinaryTree("L",
                                                new BinaryTree(),
                                                new BinaryTree("M"))),
                                new BinaryTree("N",
                                        new BinaryTree(),
                                        new BinaryTree("O")))),
                new BinaryTree("P",
                        new BinaryTree("Q"),
                        new BinaryTree("R",
                                new BinaryTree("S",
                                        new BinaryTree("T"),
                                        new BinaryTree()),
                                new BinaryTree("U"))));

        System.out.println("Tree Height = " + root.height());
        System.out.println("Tree Leaves = " + root.leafData());

        System.out.println("Tree contains A = " + root.contains("A")); //true
        System.out.println("Tree contains E = " + root.contains("E")); //true
        System.out.println("Tree contains M = " + root.contains("M")); //true
        System.out.println("Tree contains U = " + root.contains("U")); //true
        System.out.println("Tree contains Z = " + root.contains("Z")); //false
    }
}
