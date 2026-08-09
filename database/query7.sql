SELECT MIN(bloodpressure) AS MinBP , MAX(bloodpressure) AS MaxBP FROM campusx.insurance_data
WHERE diabetic = 'Yes' AND smoker = 'Yes'