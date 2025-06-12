package methods.create_register;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;

/**
 * Handles creation of records for Student, Teacher, and Subject entities.
 */
public class CreateEntity {
    private String dbUrl;

    /**
     * Loads the database connection URL from the configuration file.
     */
    public CreateEntity() {
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("src/database/DBconfiguration.properties")) {
            properties.load(input);
            dbUrl = properties.getProperty("db.url");
        } catch (IOException e) {
            System.out.println("Error loading database configuration: " + e.getMessage());
        }
    }

    /**
     * Creates a new student record by collecting input from the console.
     */
    public void createStudent() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter student DNI number (no spaces or dots): ");
            String dni = scanner.nextLine();

            System.out.print("Enter student first name: ");
            String firstName = scanner.nextLine();

            System.out.print("Enter student last name: ");
            String lastName = scanner.nextLine();

            System.out.print("Enter date of birth (format: DD-MM-YYYY): ");
            String birthDate = scanner.nextLine();

            System.out.print("Enter address: ");
            String address = scanner.nextLine();

            // Insert data into the "student" table
            try (Connection connection = DriverManager.getConnection(dbUrl)) {
                String sql = "INSERT INTO student(dni, first_name, last_name, birth_date, address) VALUES (?, ?, ?, ?, ?)";
                PreparedStatement statement = connection.prepareStatement(sql);
                statement.setString(1, dni);
                statement.setString(2, firstName);
                statement.setString(3, lastName);
                statement.setString(4, birthDate);
                statement.setString(5, address);

                int rowsInserted = statement.executeUpdate();
                if (rowsInserted > 0) {
                    System.out.println("Student record created successfully.");
                } else {
                    System.out.println("Unexpected error: Could not create student record.");
                }
            } catch (SQLException e) {
                System.out.println("Database error while creating student: " + e.getMessage());
            }
        }
    }

    /**
     * Creates a new teacher record by collecting input from the console.
     */
    public void createTeacher() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter teacher DNI number: ");
            String dni = scanner.nextLine();

            System.out.print("Enter teacher first name: ");
            String firstName = scanner.nextLine();

            System.out.print("Enter teacher last name: ");
            String lastName = scanner.nextLine();

            // Insert data into the "teacher" table
            try (Connection connection = DriverManager.getConnection(dbUrl)) {
                String sql = "INSERT INTO teacher(dni, first_name, last_name) VALUES (?, ?, ?)";
                PreparedStatement statement = connection.prepareStatement(sql);
                statement.setString(1, dni);
                statement.setString(2, firstName);
                statement.setString(3, lastName);

                int rowsInserted = statement.executeUpdate();
                if (rowsInserted > 0) {
                    System.out.println("Teacher record created successfully.");
                } else {
                    System.out.println("Unexpected error: Could not create teacher record.");
                }
            } catch (SQLException e) {
                System.out.println("Database error while creating teacher: " + e.getMessage());
            }
        }
    }

    /**
     * Creates a new subject record by collecting input from the console.
     */
    public void createSubject() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter subject DNI number: ");
            String dni = scanner.nextLine();

            System.out.print("Enter subject name: ");
            String name = scanner.nextLine();

            // Insert data into the "subject" table
            try (Connection connection = DriverManager.getConnection(dbUrl)) {
                String sql = "INSERT INTO subject(dni, name) VALUES (?, ?)";
                PreparedStatement statement = connection.prepareStatement(sql);
                statement.setString(1, dni);
                statement.setString(2, name);

                int rowsInserted = statement.executeUpdate();
                if (rowsInserted > 0) {
                    System.out.println("Subject record created successfully.");
                } else {
                    System.out.println("Unexpected error: Could not create subject record.");
                }
            } catch (SQLException e) {
                System.out.println("Database error while creating subject: " + e.getMessage());
            }
        }
    }
}
