-- What is the average claim amount for non-smoking female patients who are diabetic?
SELECT AVG(claim) FROM campusx.insurance_data
WHERE smoker = 'NO' and gender = 'female' and diabetic = 'Yes'