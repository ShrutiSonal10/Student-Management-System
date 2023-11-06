create database face_recognizer;
CREATE TABLE face_recognizer.student (
    Dep varchar(45),
    Course varchar(45),
    Year varchar(45),
    Semester varchar(45),
    Student_id int NOT NULL PRIMARY KEY,
    Name varchar(255),
    Division varchar(45),
    Roll varchar(45),
    Gender varchar(45),
    DOB varchar(45),
    Email varchar(255),
    Phone varchar(45),
    Address varchar(45),
    Teacher varchar(45),
    PhotoSample varchar(45)
);
select * from face_recognizer.student;
