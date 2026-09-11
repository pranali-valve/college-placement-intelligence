-- =========================================================
-- COLLEGE PLACEMENT INTELLIGENCE SYSTEM
-- SQL QUERIES
-- =========================================================


-- 1. TOTAL STUDENTS
SELECT COUNT(*) AS total_students
FROM students;


-- 2. TOTAL PLACED STUDENTS
SELECT COUNT(*) AS placed_students
FROM placements
WHERE placed = 1;


-- 3. TOTAL NOT PLACED STUDENTS
SELECT COUNT(*) AS not_placed_students
FROM placements
WHERE placed = 0;


-- 4. PLACEMENT RATE
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN placed = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS placement_rate
FROM placements;


-- 5. AVERAGE PACKAGE
SELECT
    ROUND(AVG(package_lpa), 2) AS average_package_lpa
FROM placements
WHERE placed = 1;


-- 6. HIGHEST PACKAGE
SELECT
    MAX(package_lpa) AS highest_package_lpa
FROM placements
WHERE placed = 1;


-- 7. BRANCH-WISE PLACEMENT
SELECT
    s.branch,
    COUNT(*) AS total_students,
    SUM(CASE WHEN p.placed = 1 THEN 1 ELSE 0 END) AS placed_students,
    ROUND(
        100.0 * SUM(CASE WHEN p.placed = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS placement_rate
FROM students s
JOIN placements p
    ON s.student_id = p.student_id
GROUP BY s.branch
ORDER BY placement_rate DESC;


-- 8. YEAR-WISE PLACEMENT
SELECT
    s.placement_year,
    COUNT(*) AS total_students,
    SUM(CASE WHEN p.placed = 1 THEN 1 ELSE 0 END) AS placed_students,
    ROUND(
        100.0 * SUM(CASE WHEN p.placed = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS placement_rate
FROM students s
JOIN placements p
    ON s.student_id = p.student_id
GROUP BY s.placement_year
ORDER BY s.placement_year;


-- 9. COMPANY-WISE HIRING
SELECT
    company,
    COUNT(*) AS students_hired
FROM placements
WHERE placed = 1
GROUP BY company
ORDER BY students_hired DESC;


-- 10. AVERAGE PACKAGE BY COMPANY
SELECT
    company,
    ROUND(AVG(package_lpa), 2) AS average_package_lpa,
    COUNT(*) AS students_hired
FROM placements
WHERE placed = 1
GROUP BY company
ORDER BY average_package_lpa DESC;


-- 11. STUDENTS WITH HIGH CGPA
SELECT
    student_id,
    branch,
    cgpa,
    technical_skills,
    internships,
    projects
FROM students
WHERE cgpa >= 8
ORDER BY cgpa DESC;


-- 12. STUDENTS WITH HIGH BACKLOG RISK
SELECT
    student_id,
    branch,
    cgpa,
    backlogs,
    internships,
    technical_skills
FROM students
WHERE backlogs >= 3
ORDER BY backlogs DESC;


-- 13. PLACEMENT-READY STUDENTS
SELECT
    s.student_id,
    s.branch,
    s.cgpa,
    s.technical_skills,
    s.internships,
    s.projects,
    s.backlogs
FROM students s
WHERE s.cgpa >= 8
  AND s.technical_skills >= 6
  AND s.internships >= 1
  AND s.backlogs = 0
ORDER BY s.cgpa DESC;


-- 14. STUDENTS NEEDING TRAINING
SELECT
    student_id,
    branch,
    cgpa,
    technical_skills,
    internships,
    projects,
    aptitude_score,
    communication_score
FROM students
WHERE
    cgpa < 8
    OR technical_skills < 6
    OR internships = 0
ORDER BY cgpa;


-- 15. TOP 10 PACKAGES
SELECT
    s.student_id,
    s.branch,
    p.company,
    p.package_lpa
FROM students s
JOIN placements p
    ON s.student_id = p.student_id
WHERE p.placed = 1
ORDER BY p.package_lpa DESC
LIMIT 10;