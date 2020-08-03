-- Create the tables as indicated in the task brief
DROP TABLE IF EXISTS DEPARTMENT;

CREATE TABLE DEPARTMENT (
  Depart_ID VARCHAR(255) NOT NULL, -- D[0-9]+
  Department_Name VARCHAR(255),
  PRIMARY KEY (Depart_ID)
);

DROP TABLE IF EXISTS EMPLOYEE;

CREATE TABLE EMPLOYEE (
  Employee_ID VARCHAR(255) NOT NULL, -- E[0-9]+
  Employee_Name VARCHAR(255),
  Hire_Date INT, -- Number of seconds since epoch (no date type in SQLite)
  Department_ID INT,
  IS_Active VARCHAR(1), -- Boolean (no boolean in SQLite)
  Employee_Last_Date INT,
  PRIMARY KEY (Employee_ID),
  FOREIGN KEY (Department_ID) REFERENCES DEPARTMENT(Depart_ID)
);