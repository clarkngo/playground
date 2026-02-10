### Answer Key for the 6 Queries

Use these exact queries to test the logic in the simulator:

1. **All rows/columns (Before):**
`SELECT * FROM customers`
2. **Customers in Ohio:**
`SELECT * FROM customers WHERE State = 'OH'`
3. **Name and Address in Westlake:**
`SELECT Name, Address FROM customers WHERE City = 'Westlake'`
4. **Change Jane Doe's Zip:**
`UPDATE customers SET Zip = '12303' WHERE Name = 'Jane Doe'`
5. **Delete Jack Hill:**
`DELETE FROM customers WHERE Name = 'Jack Hill'`
6. **All rows/columns (After):**
`SELECT * FROM customers`
