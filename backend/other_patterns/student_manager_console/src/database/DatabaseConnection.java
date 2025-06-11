package database;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.*;
import java.util.Properties;

/**
 * Handles the connection to a SQLite database and provides utility methods
 * for checking data presence and closing the connection.
 */
public class DatabaseConnection {
    private Connection connection;
    public String dbUrl;

    /**
     * Constructor that initializes the database connection using configuration properties.
     */
    public DatabaseConnection() {
        // Load database properties from configuration file
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("src/database/DBconfiguration.properties")) {
            properties.load(input);
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error: Could not load database configuration.");
        }

        // Retrieve the database URL from the loaded properties
        this.dbUrl = properties.getProperty("db.url");

        // Load SQLite JDBC driver
        try {
            Class.forName("org.sqlite.JDBC");
        } catch (ClassNotFoundException e) {
            System.out.println("Error: SQLite JDBC driver not found.");
        }

        // Establish connection to the database
        try {
            connection = DriverManager.getConnection(dbUrl);
            System.out.println("Database connection established.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    /**
     * Checks if a specific table contains any records.
     *
     * @param tableName Name of the table to check.
     * @return true if the table has at least one record; false otherwise.
     */
    public boolean hasRecords(String tableName) {
        String sql = "SELECT COUNT(*) FROM " + tableName;

        try (Connection connection = DriverManager.getConnection(dbUrl);
             PreparedStatement preparedStatement = connection.prepareStatement(sql);
             ResultSet resultSet = preparedStatement.executeQuery()) {

            if (resultSet.next()) {
                return resultSet.getInt(1) > 0;
            }
        } catch (SQLException e) {
            System.out.println("Error while checking records in table '" + tableName + "': " + e.getMessage());
        }
        return false;
    }

    /**
     * Verifies if the given table has any records, printing an error if it's empty.
     *
     * @param tableName Name of the table to verify.
     * @return true if the table has records; false otherwise.
     */
    public boolean checkRecords(String tableName) {
        if (!hasRecords(tableName)) {
            System.out.println("Error: No records found in the database. Please insert data first.");
            return false;
        }
        return true;
    }

    /**
     * Gets the current database connection instance.
     *
     * @return Active database connection.
     */
    public Connection getConnection() {
        return connection;
    }

    /**
     * Closes the current database connection if it's open.
     */
    public void closeConnection() {
        if (connection != null) {
            try {
                connection.close();
                System.out.println("Database connection closed.");
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
