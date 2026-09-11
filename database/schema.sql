-- =========================================================
-- COLLEGE PLACEMENT INTELLIGENCE SYSTEM
-- DATABASE SCHEMA
-- =========================================================

-- STUDENTS TABLE
CREATE TABLE IF NOT EXISTS students (
    student_id VARCHAR(20) PRIMARY KEY,
    branch VARCHAR(50) NOT NULL,
    cgpa DECIMAL(4,2),
    tenth_percentage DECIMAL(5,2),
    twelfth_percentage DECIMAL(5,2),
    backlogs INTEGER,
    internships INTEGER,
    projects INTEGER,
    certifications INTEGER,
    technical_skills INTEGER,
    aptitude_score DECIMAL(5,2),
    communication_score DECIMAL(5,2),
    attendance DECIMAL(5,2),
    placement_year INTEGER
);


-- PLACEMENTS TABLE
CREATE TABLE IF NOT EXISTS placements (
    placement_id SERIAL PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    placed INTEGER NOT NULL,
    company VARCHAR(100),
    package_lpa DECIMAL(6,2),

    CONSTRAINT fk_student
        FOREIGN KEY (student_id)
        REFERENCES students(student_id)
);


-- INDEX FOR FASTER STUDENT LOOKUPS
CREATE INDEX IF NOT EXISTS idx_students_branch
ON students(branch);

CREATE INDEX IF NOT EXISTS idx_students_year
ON students(placement_year);

CREATE INDEX IF NOT EXISTS idx_placements_student
ON placements(student_id);

CREATE INDEX IF NOT EXISTS idx_placements_company
ON placements(company);


-- CHECK TABLES
SELECT * FROM students LIMIT 5;

SELECT * FROM placements LIMIT 5;