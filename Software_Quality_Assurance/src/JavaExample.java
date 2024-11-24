import java.util.Scanner;

public class JavaExample {
    // Method to calculate grade based on marks
    public static String calculateGrade(int[] marks) {
        int total = 0;

        // Validate marks input
        for (int mark : marks) {
            if (mark < 0 || mark > 100) { // Check for invalid marks
                throw new IllegalArgumentException("Marks must be between 0 and 100.");
            }
            total += mark; // Add valid marks to the total
        }

        float avg = total / (float) marks.length; // Calculate average

        // Determine grade based on average
        if (avg >= 80) return "A";
        else if (avg >= 60) return "B";
        else if (avg >= 40) return "C";
        else return "D";
    }

    public static void main(String[] args) {
        int[] marks = new int[6];
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter marks for 6 subjects:");
        for (int i = 0; i < 6; i++) {
            System.out.print("Enter Marks of Subject " + (i + 1) + ": ");
            marks[i] = scanner.nextInt(); // Input marks for each subject
        }
        scanner.close();

        try {
            String grade = calculateGrade(marks); // Calculate grade
            System.out.println("The student Grade is: " + grade);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage()); // Display error message for invalid input
        }
    }
}
