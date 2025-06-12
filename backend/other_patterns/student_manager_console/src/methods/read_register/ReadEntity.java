package methods.read_register;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

import database.DatabaseConnection;

/**
 * Provides read operations for different entities in the system.
 */
public class ReadEntity extends DatabaseConnection {

    public String dbUrl;

    public ReadEntity() {
        // Load database configuration properties
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("src/database/DBconfiguration.properties")) {
            properties.load(input);
            dbUrl = properties.getProperty("db.url");
        } catch (IOException e) {
            System.out.println("Failed to load database configuration: " + e.getMessage());
        }
    }

    /**
     * Reads a student by their ID number.
     */
    public void readStudent() {
        if (!checkRecords("student")) {
            return;
        }

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter student DNI number: ");
        String dni = scanner.next();

        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String query = "SELECT * FROM student WHERE dni = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, dni);

            ResultSet result = statement.executeQuery();
            if (result.next()) {
                System.out.println("Student found:");
                System.out.println("DNI Number: " + result.getString("dni"));
                System.out.println("First Name: " + result.getString("first_name"));
                System.out.println("Last Name: " + result.getString("last_name"));
                System.out.println("Date of Birth: " + result.getString("birth_date"));
                System.out.println("Address: " + result.getString("address"));
            } else {
                System.out.println("No student found with DNI number: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Database connection error: " + e.getMessage());
        }

        scanner.close();
    }

    /**
     * Reads a teacher by their DNI number.
     */
    public void readTeacher() {
        if (!checkRecords("teacher")) {
            return;
        }

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter teacher DNI number: ");
        String dni = scanner.next();

        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String query = "SELECT * FROM teacher WHERE dni = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, dni);

            ResultSet result = statement.executeQuery();
            if (result.next()) {
                System.out.println("Teacher found:");
                System.out.println("DNI Number: " + result.getString("dni"));
                System.out.println("First Name: " + result.getString("first_name"));
                System.out.println("Last Name: " + result.getString("last_name"));
            } else {
                System.out.println("No teacher found with DNI number: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Database connection error: " + e.getMessage());
        }

        scanner.close();
    }

    /**
     * Reads a subject by its ID.
     */
    public void readSubject() {
        if (!checkRecords("subject")) {
            return;
        }

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter subject DNI number: ");
        String dni = scanner.next();

        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String query = "SELECT * FROM subject WHERE dni = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, dni);

            ResultSet result = statement.executeQuery();
            if (result.next()) {
                System.out.println("Subject found:");
                System.out.println("DNI Number: " + result.getString("dni"));
                System.out.println("Name: " + result.getString("subject_name"));
            } else {
                System.out.println("No subject found with DNI number: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Database connection error: " + e.getMessage());
        }

        scanner.close();
    }
}
