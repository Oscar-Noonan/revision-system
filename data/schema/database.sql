CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    time_available INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS enrolments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (subject_id)
        REFERENCES subjects(subject_id)
);

CREATE TABLE IF NOT EXISTS questions (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    mark_scheme TEXT NOT NULL,
    marks INTEGER NOT NULL,

    FOREIGN KEY (subject_id)
        REFERENCES subjects(subject_id)
);

CREATE TABLE IF NOT EXISTS answers (
    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    answer TEXT NOT NULL,
    marks_awarded INT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
);