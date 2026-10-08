CREATE TABLE IF NOT EXISTS students (
    studentID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    time_available INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS subjects (
    subjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    subjectName TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS enrolments (
    enrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    studentID INTEGER NOT NULL,
    subjectID INTEGER NOT NULL,

    FOREIGN KEY (studentID)
        REFERENCES students(studentID),

    FOREIGN KEY (subjectID)
        REFERENCES subjects(subjectID)
);

CREATE TABLE IF NOT EXISTS questions (
    questionID INTEGER PRIMARY KEY AUTOINCREMENT,
    subjectID INTEGER NOT NULL,
    question TEXT NOT NULL,
    markScheme TEXT NOT NULL,
    marks INTEGER NOT NULL,

    FOREIGN KEY (subjectID)
        REFERENCES subjects(subjectID)
);

CREATE TABLE IF NOT EXISTS answers (
    answerID INTEGER PRIMARY KEY AUTOINCREMENT,
    studentID INTEGER NOT NULL,
    answer TEXT NOT NULL,
    marksAwarded INT NOT NULL,

    FOREIGN KEY (studentID)
        REFERENCES students(studentID)
);