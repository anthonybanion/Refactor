import methods.create_register.CreateEntity;
import methods.read_register.ReadEntity;
import methods.update_register.UpdateEntity;
import methods.delete_register.DeleteEntity;

import java.util.Scanner;

public class StudentManagerApp {
    private static final String INVALID_OPTION_MSG = "Invalid option, please select another.";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int option;

        do {
            String mainMenu = """
                    ===============================================
                    |               STUDENT MANAGER               |
                    ===============================================
                    |                                            |
                    | Please select an option by typing the number: |
                    |                                            |
                    | 1. Create a record                         |
                    | 2. Read a record                           |
                    | 3. Update a record                         |
                    | 4. Delete a record                         |
                    | 5. Exit the program                        |
                    |____________________________________________|
                    """;
            System.out.print(mainMenu);

            // Read selected option
            System.out.print("Select an option: ");
            option = scanner.nextInt();
            scanner.nextLine(); // consume newline

            // Execute action based on selected option
            switch (option) {
                case 1:
                    System.out.println("Create a record:");
                    createRecord(scanner);
                    break;
                case 2:
                    System.out.println("Read a record:");
                    readRecord(scanner);
                    break;
                case 3:
                    System.out.println("Update a record:");
                    updateRecord(scanner);
                    break;
                case 4:
                    System.out.println("Delete a record:");
                    deleteRecord(scanner);
                    break;
                case 5:
                    System.out.println("Closing system... Thank you for using Student Manager.");
                    printAuthorInfo();
                    break;
                default:
                    System.out.println(INVALID_OPTION_MSG);
            }

        } while (option != 5);

        scanner.close();
    }

    /**
     * Menu for creating a record (Student, Professor, Subject).
     */
    public static void createRecord(Scanner scanner) {
        System.out.print("""
                Select the type of record to create:
                1. Student
                2. Professor
                3. Subject
                """);
        int type = scanner.nextInt();
        scanner.nextLine(); // consume newline

        CreateEntity createEntity = new CreateEntity();

        switch (type) {
            case 1 -> createEntity.createStudent();
            case 2 -> createEntity.createTeacher();
            case 3 -> createEntity.createSubject();
            default -> System.out.println(INVALID_OPTION_MSG);
        }
    }

    /**
     * Menu for reading a record (Student, Professor, Subject).
     */
    public static void readRecord(Scanner scanner) {
        System.out.print("""
                Select the type of record to read:
                1. Student
                2. Professor
                3. Subject
                """);
        int type = scanner.nextInt();
        scanner.nextLine(); // consume newline

        ReadEntity readEntity = new ReadEntity();

        switch (type) {
            case 1 -> readEntity.readStudent();
            case 2 -> readEntity.readTeacher();
            case 3 -> readEntity.readSubject();
            default -> System.out.println(INVALID_OPTION_MSG);
        }
    }

    /**
     * Menu for updating a record (Student, Professor, Subject).
     */
    public static void updateRecord(Scanner scanner) {
        System.out.print("""
                Select the type of record to update:
                1. Student
                2. Professor
                3. Subject
                """);
        int type = scanner.nextInt();
        scanner.nextLine(); // consume newline

        UpdateEntity updateEntity = new UpdateEntity();

        switch (type) {
            case 1 -> updateEntity.updateStudent();
            case 2 -> updateEntity.updateProfessor();
            case 3 -> updateEntity.updateSubject();
            default -> System.out.println(INVALID_OPTION_MSG);
        }
    }

    /**
     * Menu for deleting a record or all records.
     */
    public static void deleteRecord(Scanner scanner) {
        System.out.print("""
                Select the type of record to delete:
                1. Student
                2. Professor
                3. Subject
                4. Delete all records
                """);
        int type = scanner.nextInt();
        scanner.nextLine(); // consume newline

        DeleteEntity deleteEntity = new DeleteEntity();

        switch (type) {
            case 1 -> deleteEntity.deleteStudent();
            case 2 -> deleteEntity.deleteProfessor();
            case 3 -> deleteEntity.deleteSubject();
            case 4 -> deleteEntity.deleteAllRecords();
            default -> System.out.println(INVALID_OPTION_MSG);
        }
    }

    /**
     * Prints author and application information upon exit.
     */
    private static void printAuthorInfo() {
        String authorInfo = """
                 ********************************************************************************
                 *                           STUDENT MANAGER v01                                *
                 ********************************************************************************
                 *      Mariano Maldonado                                                       *
                 *      { DEV</>CODE } Informatic Solutions                                     *
                 *      LinkedIn: https://www.linkedin.com/in/mariano-maldonado-810847288/      *
                 *      Instagram: https://www.instagram.com/marianomaldonado.dev/              *
                 *      GitHub: https://github.com/MarianoMaldonado-dev                         *
                 *                                                                              *
                 ********************************************************************************
                """;
        System.out.println(authorInfo);
    }
}
