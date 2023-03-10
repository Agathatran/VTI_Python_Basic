DROP DATABASE IF EXISTS STUDENT_DB;
CREATE DATABASE STUDENT_DB;
USE STUDENT_DB;
DROP TABLE IF EXISTS STUDENT_INFO
CREATE TABLE STUDENT_INFO(
				STUDENT_NUMBER INT AUTO_INCREMENT PRIMARY KEY,
				FULL_NAME VARCHAR(100) NOT NULL, 
				DATE_OF_BIRTH DATE,
				SEX ENUM('F','M'),
				ADDRESS VARCHAR(1000),
				PHONE_NUMBER CHAR(11),
				EMAIL VARCHAR(50)
);
DROP TABLE IF EXISTS SUBJECTS
CREATE TABLE SUBJECTS(
					SUBJECT_NO VARCHAR(50) PRIMARY KEY,
                    SUBJECT_NAME VARCHAR(50)
);
DROP TABLE IF EXISTS GRADING
CREATE TABLE GRADING(
					STUDENT_NUMBER INT,
                    SUBJECT_NO. VARCHAR(50),
                    ASSIGNMENT FLOAT NOT NULL,
                    FINAL_GRADE FLOAT NOT NULL,
                    FOREIGN KEY (STUDENT_NUMBER) REFERENCES STUDENT_INFO(STUDENT_NUMBER)
                    FOREIGN KEY (SUBJECT_NO) REFERENCES SUBJECTS(SUBJECT_NO)
);

