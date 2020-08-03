-- Write a query to select all the active employees who joined “Production 
-- Support” job family in Jun 2002, Apr 1995 and Jun 2004.
SELECT * 
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.Department_ID = D.Depart_ID
    AND D.Department_Name = "Production Support"
    AND (E.Hire_Date LIKE '%Jun-2002' 
        OR E.Hire_Date LIKE '%Apr-1995' 
        OR E.Hire_Date LIKE '%Jun-2004')
    AND IS_Active = 'Y';