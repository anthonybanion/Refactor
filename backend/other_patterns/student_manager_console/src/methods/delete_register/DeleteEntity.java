package methods.delete_register;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

/**
 * Handles deletion of records for Student, Professor, and Subject entities.
 */
public class DeleteEntity {
    private String dbUrl;

    /**
     * Loads the database connection URL from the configuration file.
     */
    public DeleteEntity() {
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("src/database/DBconfiguration.properties")) {
            properties.load(input);
            dbUrl = properties.getProperty("db.url");
        } catch (IOException e) {
            System.out.println("Error loading database configuration: " + e.getMessage());
        }
    }

    /**
     * Deletes a student record by DNI after checking if students exist.
     */
    public void deleteStudent() {
        if (!hasRecords("student")) {
            System.out.println("No student records found to delete.");
            return;
        }

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the student's DNI to delete: ");
            int dni = scanner.nextInt();

            try (Connection connection = DriverManager.getConnection(dbUrl)) {
                String sql = "DELETE FROM student WHERE student_dni = ?";
                PreparedStatement statement = connection.prepareStatement(sql);
                statement.setInt(1, dni);

                int rowsDeleted = statement.executeUpdate();
                if (rowsDeleted > 0) {
                    System.out.println("Student record deleted successfully.");
                } else {
                    System.out.println("No student found with DNI: " + dni);
                }
            } catch (SQLException e) {
                System.out.println("Database error while deleting student: " + e.getMessage());
            }
        }
    }

    /**
     * Deletes a professor record by ID after checking if professors exist.
     */
    public void deleteProfessor() {
        if (!hasRecords("professor")) {
            System.out.println("No professor records found to delete.");
            return;
        }

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the professor's ID to delete: ");
            int id = scanner.nextInt();

            try (Connection connection = DriverManager.getConnection(dbUrl)) {
                String sql = "DELETE FROM professor WHERE professor_id = ?";
                PreparedStatement statement = connection.prepareStatement(sql);
                statement.setInt(1, id);

                int rowsDeleted = statement.executeUpdate();
                if (rowsDeleted > 0) {
                    System.out.println("Professor record deleted successfully.");
                } else {
                    System.out.println("No professor found with ID: " + id);
                }
            } catch (SQLException e) {
                System.out.println("Database error while deleting professor: " + e.getMessage());
            }
        }
    }

    /**
     * Deletes a subject record by ID after checking if subjects exist.
     */
    public void deleteSubject() {
        if (!hasRecords("subject")) {
            System.out.println("No subject records found to delete.");
            return;
        }

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the subject ID to delete: ");
            int id = scanner.nextInt();

            try (Connection connection = DriverManager.getConnection(dbUrl)) {
                String sql = "DELETE FROM subject WHERE subject_id = ?";
                PreparedStatement statement = connection.prepareStatement(sql);
                statement.setInt(1, id);

                int rowsDeleted = statement.executeUpdate();
                if (rowsDeleted > 0) {
                    System.out.println("Subject record deleted successfully.");
                } else {
                    System.out.println("No subject found with ID: " + id);
                }
            } catch (SQLException e) {
                System.out.println("Database error while deleting subject: " + e.getMessage());
            }
        }
    }

    /**
     * Deletes all records from all tables after user confirmation.
     */
    public void deleteAllRecords() {
        try (Scanner scanner = new Scanner(System.in)) {
            if (!hasRecords("student") && !hasRecords("professor") && !hasRecords("subject")) {
                System.out.println("Error: No records found. Please add data first.");
                return;
            }

            System.out.println("⚠️ WARNING! THIS ACTION WILL DELETE ALL RECORDS IN THE DATABASE.");
            System.out.println("ARE YOU SURE YOU WANT TO PROCEED?");
            System.out.println("1. YES");
            System.out.println("2. NO");

            int choice = scanner.nextInt();

            if (choice == 1) {
                try (Connection connection = DriverManager.getConnection(dbUrl)) {
                    String[] tables = {"student", "professor", "subject", "student_subject"};
                    for (String table : tables) {
                        String sql = "DELETE FROM " + table;
                        try (PreparedStatement statement = connection.prepareStatement(sql)) {
                            int rowsDeleted = statement.executeUpdate();
                            System.out.println("Deleted " + rowsDeleted + " records from table: " + table);
                        }
                    }
                    System.out.println("✅ All records deleted successfully.");
                } catch (SQLException e) {
                    System.out.println("Database error while deleting all records: " + e.getMessage());
                }
            } else if (choice == 2) {
                System.out.println("Operation cancelled. No records were deleted.");
            } else {
                System.out.println("Invalid choice. Please enter 1 or 2.");
            }
        }
    }

    /**
     * Helper method to check if there are any records in a given table.
     * @param tableName The table to check (in English, singular form).
     * @return true if records exist, false otherwise.
     */
    private boolean hasRecords(String tableName) {
        String query = "";
        switch (tableName.toLowerCase()) {
            case "student":
                query = "SELECT 1 FROM student LIMIT 1";
                break;
            case "professor":
                query = "SELECT 1 FROM professor LIMIT 1";
                break;
            case "subject":
                query = "SELECT 1 FROM subject LIMIT 1";
                break;
            default:
                return false;
        }

        try (Connection connection = DriverManager.getConnection(dbUrl);
             PreparedStatement statement = connection.prepareStatement(query)) {
            return statement.executeQuery().next();
        } catch (SQLException e) {
            System.out.println("Database error while checking records in table " + tableName + ": " + e.getMessage());
            return false;
        }
    }
}
