-- Write a SQL query to delete all records for patients who are smokers and have no children.
DELETE FROM campusx.insurance_data
WHERE smoker = 'Yes' AND children = '0'
