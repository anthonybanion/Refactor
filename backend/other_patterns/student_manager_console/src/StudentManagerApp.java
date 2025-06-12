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
                    |                                             |
                    |    Select an option by typing the number:   |
                    |                                             |
                    | 1. Create a record                          |
                    | 2. Read a record                            |
                    | 3. Update a record                          |
                    | 4. Delete a record                          |
                    | 5. Exit the program                         |
                    |_____________________________________________|
                    """;
            System.out.print(mainMenu);

            // Read selected option
            option = getValidatedIntInput(scanner, "Select an option (1-5): ");
            if (option == -1) continue;

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
     * Validates and returns an integer input from the user.
     *
     * param scanner Scanner object to read input
     * param prompt  Prompt message to display to the user
     * return Validated integer input
     */

    public static int getValidatedIntInput(Scanner scanner, String prompt) {
        System.out.print(prompt);
        scanner.nextLine();
        try {
            if (scanner.hasNextLine()) {
                String line = scanner.nextLine().trim();
                if (line.matches("\\d+")) {
                    return Integer.parseInt(line);
                } else {
                    System.out.println("❌ Invalid input. Please enter a valid number.");
                    return -1;
                }
            } else {
                System.out.println("❌ No input detected. Exiting.");
                return -1;
            }
        } catch (Exception e) {
            System.out.println("❌ Error reading input: " + e.getMessage());
            return -1;
        }
    }


    /**
     * Menu for creating a record (Student, Professor, Subject).
     */
    public static void createRecord(Scanner scanner) {
        int type; 
        System.out.print("""
                Select the type of record to create:
                1. Student
                2. Professor
                3. Subject
                """);

        type = getValidatedIntInput(scanner, "Select the type of record to create (1-3): ");
        if (type == -1) return;

        CreateEntity createEntity = new CreateEntity();

        switch (type) {
            case 1 : 
                createEntity.createStudent(scanner);
                break;
            case 2 : 
                createEntity.createTeacher(scanner);
                break;
            case 3 : 
                createEntity.createSubject(scanner);
                break;
            default : 
                System.out.println(INVALID_OPTION_MSG);
        }
    }

    /**
     * Menu for reading a record (Student, Professor, Subject).
     */
    public static void readRecord(Scanner scanner) {
        int type;
        System.out.print("""
                Select the type of record to read:
                1. Student
                2. Professor
                3. Subject
                """);
        
        type = getValidatedIntInput(scanner, "Select the type of record to read (1-3): ");
        if (type == -1) return;

        ReadEntity readEntity = new ReadEntity();

        switch (type) {
            case 1 : 
                readEntity.readStudent(scanner);
                break;
            case 2 : 
                readEntity.readTeacher(scanner);
                break;
            case 3 : 
                readEntity.readSubject(scanner);
                break;
            default : System.out.println(INVALID_OPTION_MSG);
        }
    }

    /**
     * Menu for updating a record (Student, Professor, Subject).
     */
    public static void updateRecord(Scanner scanner) {
        int type;
        System.out.print("""
                Select the type of record to update:
                1. Student
                2. Professor
                3. Subject
                """);

        type = getValidatedIntInput(scanner, "Select the type of record to update (1-3): ");
        if (type == -1) return;

        UpdateEntity updateEntity = new UpdateEntity();

        switch (type) {
            case 1 : 
                updateEntity.updateStudent(scanner);
                break;
            case 2 : 
                updateEntity.updateTeacher(scanner);
                break;
            case 3 : 
                updateEntity.updateSubject(scanner);
                break;
            default : 
                System.out.println(INVALID_OPTION_MSG);
        }
    }

    /**
     * Menu for deleting a record or all records.
     */
    public static void deleteRecord(Scanner scanner) {
        int type;
        System.out.print("""
                Select the type of record to delete:
                1. Student
                2. Professor
                3. Subject
                4. Delete all records
                """);
        
        type = getValidatedIntInput(scanner, "Select the type of record to delete (1-4): ");
        if (type == -1) return;

        DeleteEntity deleteEntity = new DeleteEntity();

        switch (type) {
            case 1 : 
                deleteEntity.deleteStudent(scanner);
                break;
            case 2 : 
                deleteEntity.deleteTeacher(scanner);
                break;
            case 3 : 
                deleteEntity.deleteSubject(scanner);
                break;
            case 4 : 
                deleteEntity.deleteAllRecords(scanner);
                break;
            default : 
                System.out.println(INVALID_OPTION_MSG);
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
