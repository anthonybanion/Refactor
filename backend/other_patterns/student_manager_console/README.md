# Student Administration Console – SQLite CRUD Application

## 📌 Introduction

**Student Administration Console** is a Java-based CRUD (Create, Read, Update, Delete) application designed to manage student records using `SQLite` as the database. This project demonstrates core Java programming concepts, JDBC connectivity, and file-based database management in a simple yet functional console application.

Key Features:

- **✔ Create** new student records
- **✔ Read**/List existing student data
- **✔ Update** student information
- **✔ Delete** student records
- **✔ SQLite** Integration for lightweight database management

## 🎯 Objectives

1. Provide a `user-friendly` console interface for managing student data.
2. Implement `persistent storage` using SQLite without requiring a server.
3. Demonstrate `JDBC best practices` (connections, prepared statements, error handling).
4. Maintain a clean `modular structure` for scalability.

## 📂 Project Structure

```text
Refactor/
└── backend/
    └── other_patterns/
        └── student_administration_console/
            ├── bin/                                # Compiled .class files
            ├── database/                           # SQLite database file
            │   └── student_manager.db
            ├── src/
            │   ├── database/                       # Database handling
            │   │   ├── DBconfiguration.properties
            │   │   └── DatabaseConnection.java
            │   ├── methods/                        # CRUD operations
            │   │   ├── Create.java
            │   │   ├── Delete.java
            │   │   ├── Read.java
            │   │   └── Update.java
            │   └── StudentManagerApp.java          # Main class
            └── lib/                                # Dependencies (SQLite JDBC)
```

## ⚙️ Setup & Execution

Prerequisites:

- Java JDK 11+
- SQLite JDBC driver (`sqlite-jdbc-3.50.1.0.jar`)

Steps:

1. **Clone the repository:**

```bash
git clone https://github.com/anthonybanion/Learning.git
```

2. **Compile the project:**

From the root (`Java/`):

```bash
javac -cp "Refactor/backend/other*backend_patterns/student_administration_console/lib/sqlite-jdbc-3.50.1.0.jar" \
 -d Refactor/backend/other_backend_patterns/student_administration_console/bin/ \
 Refactor/backend/other_backend_patterns/student_administration_console/src/*.java \
 Refactor/backend/other*backend_patterns/student_administration_console/src/methods/\*\*/*.java \
 Refactor/backend/other_backend_patterns/student_administration_console/src/database/\*.java
```

3. **Run the application:**

```bash

java -cp "Refactor/backend/other_backend_patterns/student_administration_console/lib/sqlite-jdbc-3.50.1.0.jar" \
 projects.small_projects.student_manager.src.StudentManagerApp
```

## 🛠️ Configuration

Edit DBconfiguration.properties to customize the database path:

```python
# Path is relative to the project root
db.driver=org.sqlite.JDBC
db.url=jdbc:sqlite:database/student_manager.db
```

> 💡 Note: The database/ folder will auto-create on first run if permissions allow.

## 🧩 Modules Overview

1. DatabaseConnection.java

- Handles SQLite connection lifecycle.
- Uses `Properties` to load configuration.

2. **CRUD Operations**
   |Class |Functionality|
   |------|-------------|
   |Create| Adds new students via console input.|
   |Read |Lists all students or filters by ID.|
   |Update| Modifies existing student records.|
   |Delete| Removes students by ID.|

3. StudentManagerApp.java

- Main menu driver with switch-case logic.
- Catches SQL/IO exceptions gracefully.

## 🐛 Troubleshooting

| Issue                       | Solution                             |
| --------------------------- | ------------------------------------ |
| "DBconfiguration not found" | Ensure the file is in src/database/. |
| SQLite permissions error    | Run chmod +w database/ in terminal.  |
| JDBC driver not loaded      | Verify JAR path in -cp argument.     |

## 📜 License

MIT License - Free for educational and personal use.

## 👏 Credits

**Original Project:** Developed by [Mariano Maldonado](https://github.com/MarianoMaldonado-dev) as part of a Java learning path ([Source Repository](https://github.com/MarianoMaldonado-dev/StudentManager)).

**Refactored/Adapted Version:** Modified by [Anthony Bañon](https://github.com/anthonybanion) with enhancements to database configuration, error handling, and project structure.

**Dependencies:**

SQLite JDBC driver provided by [Xerial](https://github.com/xerial/sqlite-jdbc).
