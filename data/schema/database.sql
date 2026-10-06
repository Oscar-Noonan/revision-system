CREATE TABLE IF NOT EXISTS students (
    studentID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    dbHash TEXT NOT NULL,
    time_available INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS subjects (
    subjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    subjectName TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS enrollments (
    enrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    studentID INTEGER NOT NULL,
    subjectID INTEGER NOT NULL,

    FOREIGN KEY (studentID)
        REFERENCES students(studentID),

    FOREIGN KEY (subjectID)
        REFERENCES subjects(subjectID)
);