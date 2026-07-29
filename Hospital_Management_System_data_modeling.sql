                       -- Practical Exercise: Hospital Managemnet System --

-- "Hospital chahti hai track kare: har patient ka har appointment kis doctor ke saath tha, kis department mein, kya diagnosis
-- hua, kitni fee charge hui, aur patient ne appointment ka feedback rating (1-5) diya."
-- Business process kya hai?
-- Grain kya hogi?
-- Facts/measures kaunse honge?
-- Dimensions kaunsi honge, aur unke attributes kya honge?
-- Kis dimension mein SCD Type 2 zaroori ho sakta hai, aur kyun? (Hint: doctor apna department change kar sakta hai)
-- Star ya Snowflake — is case mein kaunsa behtar hoga aur kyun?

                         -- SQL IMPLEMENTATION OF THESE QUESTIONS --
                                 -- DIMENSION TABLES
-- Dim_Date
CREATE TABLE Dim_Date (
    date_id      SERIAL PRIMARY KEY,      -- surrogate key
    full_date    DATE NOT NULL UNIQUE,
    day          INT,
    month        INT,
    quarter      INT,
    year         INT
);
INSERT INTO Dim_Date (full_date, day, month, quarter, year) 
VALUES 
    ('2026-01-01', 1, 1, 1, 2026),
    ('2026-01-15', 15, 1, 1, 2026),
    ('2026-02-10', 10, 2, 1, 2026),
    ('2026-03-23', 23, 3, 1, 2026),
    ('2026-04-14', 14, 4, 2, 2026);
	
-- Dim_Doctor (with SCD Type 2 support)
CREATE TABLE Dim_Doctor (
    doctor_id           SERIAL PRIMARY KEY,     -- surrogate key
    doctor_natural_id    VARCHAR(20) NOT NULL,   -- natural key (hospital's own ID)
    name                 VARCHAR(100),
    specialization       VARCHAR(100),
    department_id        INT REFERENCES Dim_Department(department_id),
    effective_date        DATE NOT NULL,
    end_date              DATE,
    is_current            BOOLEAN DEFAULT TRUE
);
INSERT INTO Dim_Doctor (doctor_natural_id, name, specialization, department_id, effective_date, end_date, is_current) 
VALUES 
    ('DOC-101', 'Dr. Muhammad Ali', 'Cardiologist', 1, '2023-01-01', NULL, TRUE),
    ('DOC-102', 'Dr. Fatima Khan', 'Neurologist', 2, '2022-05-15', NULL, TRUE),
    ('DOC-103', 'Dr. Tariq Mahmood', 'Pediatrician', 3, '2021-09-01', NULL, TRUE),
    ('DOC-104', 'Dr. Ayesha Rehman', 'Orthopedic Specialist', 4, '2020-03-10', NULL, TRUE),
    ('DOC-105', 'Dr. Usman Ahmed', 'General Surgeon', 5, '2024-02-01', NULL, TRUE);

-- Dim_Department
CREATE TABLE Dim_Department (
    department_id    SERIAL PRIMARY KEY,
    department_name  VARCHAR(100),
    building          VARCHAR(50)
);
INSERT INTO Dim_Department (department_name, building) 
VALUES 
    ('Cardiology', 'Block A'),
    ('Neurology', 'Block B'),
    ('Pediatrics', 'Block C'),
    ('Orthopedics', 'Block A'),
    ('General Surgery', 'Block D');
	
-- Dim_Patient
CREATE TABLE Dim_Patient (
    patient_id           SERIAL PRIMARY KEY,
    patient_natural_id   VARCHAR(20) NOT NULL,
    name                  VARCHAR(100),
    age                   INT,
    gender                VARCHAR(10)
);
INSERT INTO Dim_Patient (patient_natural_id, name, age, gender) 
VALUES 
    ('PAT-501', 'Zainab Bibi', 34, 'Female'),
    ('PAT-502', 'Bilal Hussain', 45, 'Male'),
    ('PAT-503', 'Sana Malik', 28, 'Female'),
    ('PAT-504', 'Hamza Sheikh', 52, 'Male'),
    ('PAT-505', 'Mariam Farooq', 19, 'Female');

                                          --FACT TABLE
CREATE TABLE Fact_Appointment (
    appointment_id     SERIAL PRIMARY KEY,
    patient_id          INT NOT NULL REFERENCES Dim_Patient(patient_id),
    doctor_id           INT NOT NULL REFERENCES Dim_Doctor(doctor_id),
    department_id       INT NOT NULL REFERENCES Dim_Department(department_id),
    date_id             INT NOT NULL REFERENCES Dim_Date(date_id),
    diagnosis            VARCHAR(200),
    fee                  DECIMAL(10,2),                                      -- measure
    feedback_rating      INT CHECK (feedback_rating BETWEEN 1 AND 5)         -- measure
);

                                   -- SCD Type 2 Insert Logic
-- Step A: Purani row ko "inactive" mark karo
UPDATE Dim_Doctor
SET end_date = CURRENT_DATE - 1,
    is_current = FALSE
WHERE doctor_natural_id = 'DOC-103' AND is_current = TRUE;

-- Step B: Nayi row insert karo
INSERT INTO Dim_Doctor (doctor_natural_id, name, specialization, department_id, effective_date, end_date, is_current)
VALUES ('DOC-103', 'Dr. Ahmed', 'Neurologist', 5, CURRENT_DATE, NULL, TRUE);

SELECT * from Dim_Doctor;

                                       -- ANALYSIS
--har dept ki avg feedback rating
SELECT d.department_name, AVG(f.feedback_rating) AS avg_rating
FROM Fact_Appointment f
JOIN Dim_Department d ON f.department_id = d.department_id
GROUP BY d.department_name
ORDER BY avg_rating DESC;

--Har doctor ki total earnings (sirf current department ke saath)
SELECT doc.name, doc.specialization, SUM(f.fee) AS total_earnings
FROM Fact_Appointment f
JOIN Dim_Doctor doc ON f.doctor_id = doc.doctor_id
WHERE doc.is_current = TRUE
GROUP BY doc.name, doc.specialization
ORDER BY total_earnings DESC;

--Monthly appointment trend
SELECT dt.year, dt.month, COUNT(*) AS total_appointments
FROM Fact_Appointment f
JOIN Dim_Date dt ON f.date_id = dt.date_id
GROUP BY dt.year, dt.month
ORDER BY dt.year, dt.month;

--har doctor ne kitne unique patients dekhen hain
SELECT doc.doctor_natural_id, COUNT(DISTINCT f.patient_id) AS unique_patients_count
FROM Fact_Appointment f
JOIN Dim_Doctor doc ON f.doctor_id = doc.doctor_id
GROUP BY doc.doctor_natural_id;

--Sabse zyada fee charge karne wala top 3 department
SELECT d.department_name,SUM(f.fee) AS total_fee
FROM Fact_Appointment f
JOIN Dim_Department d ON f.department_id=d.department_id
GROUP BY d.department_name
ORDER BY total_fee DESC
limit 3;

