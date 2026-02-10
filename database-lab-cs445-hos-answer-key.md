### Answer Key for the 7 Queries

Use these exact queries to test the logic in the simulator:

1. **Create Table:**
```
CREATE TABLE employee (
    id int NOT NULL PRIMARY KEY,
    name varchar(255) NOT NULL,
    email varchar(255),
    gender varchar(255),
    designation varchar(255)
);

```
2. **Insert Data:**
```
INSERT INTO employee (id, name, email, gender, designation) VALUES
(1, 'Alice', 'alice@xyz.com', 'M', 'Software Developer'),
(2, 'John', 'john@xyz.com', 'M', 'Software Manager'),
(3, 'Ajay', 'ajay@xyz.com', 'M', 'Software Developer'),
(4, 'Polina', 'polina@xyz.com', 'F', 'Sales Manager'),
(5, 'Henry', 'henry@xyz.com', 'M', 'Senior Software Manager');
```

3. **Read Data:**
```
SELECT *  

FROM employee  

WHERE designation = 'Software Developer'

```
4. **Update Data:**
```
UPDATE employee  

SET designation= 'Senior Software Developer'  

WHERE id = 1

```

5. **Find One:**
```
SELECT * 
FROM employee 
WHERE id=1
```
6. **Delete One:**
```
DELETE 
FROM employee 
WHERE id =3;
```

7. **Verify:**

```
SELECT * 
FROM employee
```
