-- No of patient having normal blood pressure. Normal range[90-120] 
SELECT count(bloodpressure) FROM campusx.insurance_data
WHERE bloodpressure >90 AND bloodpressure < 120