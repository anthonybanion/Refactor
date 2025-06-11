package methods.update_register;

import java.sql.*;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;
import database.DatabaseConnection;

public class UpdateEntity extends DatabaseConnection {
    public String dbUrl;

    public UpdateEntity() {
        // Cargar propiedades
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("database/DBconfiguration.properties")) {
            properties.load(input);
            dbUrl = properties.getProperty("db.url");
        } catch (IOException e) {
            System.out.println("Error al cargar las propiedades de la base de datos: " + e.getMessage());
        }
    }

    public void updateStudent() {
        if (!checkRecords("alumno")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el DNI del alumno a actualizar: ");
        int dni = scanner.nextInt();
        scanner.nextLine(); // Limpiar el buffer

        System.out.print("Ingrese el nuevo nombre del alumno: ");
        String nombre = scanner.nextLine();

        System.out.print("Ingrese el nuevo apellido del alumno: ");
        String apellido = scanner.nextLine();

        System.out.print("Ingrese la nueva fecha de nacimiento del alumno (Formato esperado: AAAA-MM-DD): ");
        String fechaNacimiento = scanner.nextLine();

        System.out.print("Ingrese la nueva dirección del alumno: ");
        String direccion = scanner.nextLine();

        // Estableciendo conexión a DB y ejecutar la actualización
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "UPDATE alumno SET nombre_alumno = ?, apellido_alumno = ?, fecha_nacimiento = ?, direccion = ? WHERE id_alumnoDNI = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, nombre);
            preparedStatement.setString(2, apellido);
            preparedStatement.setString(3, fechaNacimiento);
            preparedStatement.setString(4, direccion);
            preparedStatement.setInt(5, dni);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro del alumno fue actualizado exitosamente.");
            } else {
                System.out.println("No se encontró el alumno con DNI: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
    scanner.close();
    }

    public void updateProfessor() {
        if (!checkRecords("profesor")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el ID del profesor a actualizar: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Limpiar el buffer

        System.out.print("Ingrese el nuevo nombre del profesor: ");
        String nombre = scanner.nextLine();

        System.out.print("Ingrese el nuevo apellido del profesor: ");
        String apellido = scanner.nextLine();

        // Estableciendo conexión a DB y ejecutar la actualización
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "UPDATE profesor SET nombre_profesor = ?, apellido_profesor = ? WHERE id_profesorDNI = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, nombre);
            preparedStatement.setString(2, apellido);
            preparedStatement.setInt(3, id);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro del profesor fue actualizado exitosamente.");
            } else {
                System.out.println("No se encontró el profesor con ID: " + id);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
    scanner.close();
    }

    public void updateSubject() {
        if (!checkRecords("materia")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el ID de la materia a actualizar: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Limpiar el buffer

        System.out.print("Ingrese el nuevo nombre de la materia: ");
        String nombre = scanner.nextLine();

        // Estableciendo conexión a DB y ejecutar la actualización
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "UPDATE materia SET nombre_materia = ? WHERE id_materia = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, nombre);
            preparedStatement.setInt(2, id);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro de la materia fue actualizado exitosamente.");
            } else {
                System.out.println("No se encontró la materia con ID: " + id);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
    scanner.close();
    }
}