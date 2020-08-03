-- Insert data as given in task brief
INSERT INTO DEPARTMENT (Depart_ID, Department_Name)
VALUES 
    ("D1", "Architecture"),
    ("D2", "Scrum Master"),
    ("D3", "Production Support"),
    ("D4", "Software Engineering");

INSERT INTO EMPLOYEE (Employee_ID, Employee_Name, Hire_Date, Department_ID, IS_Active, Employee_Last_Date)
VALUES 
    ('E1', 'Glen', '06-Mar-1994', 'D1', 'Y' , NULL),
    ('E2', 'Rekha', '15-Apr-1995', 'D3', 'Y' , NULL),
    ('E3', 'Sara', '06-Apr-1994', 'D3', 'N' ,'06-Jun-1996'),
    ('E4', 'Natasha', '14-Jun-2001', 'D4', 'Y' , NULL),
    ('E5', 'Svetlana', '05-Aug-2004', 'D3', 'Y' , NULL),
    ('E6', 'Mark', '08-May-1996', 'D1', 'N' ,'09-Apr-1997'),
    ('E7', 'Sabina', '14-Jun-2002', 'D3', 'Y' , NULL),
    ('E8', 'Darrel', '05-Aug-2005', 'D3', 'Y' , NULL),
    ('E9', 'Kwong', '08-May-1997', 'D4', 'N' ,'09-May-1998'),
    ('E10', 'Amina', '14-Jun-2003', 'D3', 'Y' , NULL),
    ('E11', 'Sarita', '05-Aug-2006', 'D1', 'Y' , NULL),
    ('E12', 'Mary', '08-May-1998', 'D3', 'N' ,'28-May-2010'),
    ('E13', 'Nick', '14-Jun-2004', 'D3', 'Y' , NULL);