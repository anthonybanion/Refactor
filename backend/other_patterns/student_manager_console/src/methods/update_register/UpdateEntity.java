package methods.update_register;

import java.sql.*;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;
import database.DatabaseConnection;

/**
 * Handles update operations for Student, Teacher, and Subject entities.
 */
public class UpdateEntity extends DatabaseConnection {
    private String dbUrl;

    /**
     * Loads the database connection URL from the configuration file.
     */
    public UpdateEntity() {
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("src/database/DBconfiguration.properties")) {
            properties.load(input);
            dbUrl = properties.getProperty("db.url");
        } catch (IOException e) {
            System.out.println("Error loading database properties: " + e.getMessage());
        }
    }

    /**
     * Updates a student record based on the provided DNI.
     */
    public void updateStudent(Scanner scanner) {
        if (!checkRecords("student")) {
            return;
        }

        System.out.print("Enter the student's DNI to update: ");
        String dni = scanner.nextLine();

        System.out.print("Enter the new first name: ");
        String firstName = scanner.nextLine();

        System.out.print("Enter the new last name: ");
        String lastName = scanner.nextLine();

        System.out.print("Enter the new birth date (Format: YYYY-MM-DD): ");
        String birthDate = scanner.nextLine();

        System.out.print("Enter the new address: ");
        String address = scanner.nextLine();

        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = """
                UPDATE student
                SET first_name = ?, last_name = ?, birth_date = ?, address = ?
                WHERE dni = ?;
            """;
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, firstName);
            statement.setString(2, lastName);
            statement.setString(3, birthDate);
            statement.setString(4, address);
            statement.setString(5, dni);

            int rowsAffected = statement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ Student record updated successfully.");
            } else {
                System.out.println("⚠️ No student found with DNI: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Database error while updating student: " + e.getMessage());
        }
    }

    /**
     * Updates a teacher record based on the provided DNI.
     */
    public void updateTeacher(Scanner scanner) {
        if (!checkRecords("teacher")) {
            return;
        }

        System.out.print("Enter the teacher's DNI to update: ");
        String dni = scanner.nextLine();

        System.out.print("Enter the new first name: ");
        String firstName = scanner.nextLine();

        System.out.print("Enter the new last name: ");
        String lastName = scanner.nextLine();

        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = """
                UPDATE teacher
                SET first_name = ?, last_name = ?
                WHERE dni = ?;
            """;
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, firstName);
            statement.setString(2, lastName);
            statement.setString(3, dni);

            int rowsAffected = statement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ Teacher record updated successfully.");
            } else {
                System.out.println("⚠️ No teacher found with DNI: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Database error while updating teacher: " + e.getMessage());
        }
    }

    /**
     * Updates a subject record based on the provided DNI.
     */
    public void updateSubject(Scanner scanner) {
        if (!checkRecords("subject")) {
            return;
        }

        System.out.print("Enter the subject's DNI to update: ");
        String dni = scanner.nextLine();

        System.out.print("Enter the new subject name: ");
        String name = scanner.nextLine();

        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = """
                UPDATE subject
                SET name = ?
                WHERE dni = ?;
            """;
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, name);
            statement.setString(2, dni);

            int rowsAffected = statement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ Subject record updated successfully.");
            } else {
                System.out.println("⚠️ No subject found with DNI: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Database error while updating subject: " + e.getMessage());
        }
    }
}
