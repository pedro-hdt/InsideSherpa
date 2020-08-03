--Write a query to count number of employee who left the organization. 
SELECT COUNT(*)
FROM EMPLOYEE E
WHERE E.Employee_Last_Date IS NOT NULL;