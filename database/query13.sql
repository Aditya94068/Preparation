-- No of pateint belo 17 years of age having normal blood pressure as per below formula

   --  BP normal range = 80+(age in years × 2) to 100 + (age in years × 2)

    -- Note: Formula taken just for practice, don't take in real sense.
 
SELECT age FROM campusx.insurance_data

WHERE age < 17 AND bloodpressure between (80 + age * 2) and (100 + age * 2)