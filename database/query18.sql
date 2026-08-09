SELECT * FROM campusx.insurance_data;

SELECT DISTINCT(region) From campusx.insurance_data;

SELECT COUNT(DISTINCT(gender)) FROM campusx.insurance_data;

SELECT DISTINCT(smoker) FROM campusx.insurance_data;

SELECT DISTINCT gender,smoker FROM campusx.insurance_data;


SELECT DISTINCT bmi FROM campusx.insurance_data
ORDER BY bmi DESC;


SELECT COUNT(DISTINCT PatientID , claim) FROM campusx.insurance_data;

SELECT COUNT(DISTINCT region,diabetic) FROM campusx.insurance_data;


SELECT DISTINCT smoker,  region FROM campusx.insurance_data;


SELECT DISTINCT * FROM campusx.insurance_data;

SELECT * FROM campusx.insurance_data
WHERE gender = 'male';

SELECT * FROM campusx.insurance_data
WHERE gender = 'female';

SELECT * FROM campusx.insurance_data
WHERE smoker = 'Yes';

SELECT * FROM campusx.insurance_data
WHERE age > 50;

SELECT * FROM campusx.insurance_data
WHERE bmi < 25;

SELECT * FROM campusx.insurance_data
WHERE gender = 'female' AND smoker = 'No';

SELECT * FROM campusx.insurance_data
WHERE age BETWEEN 30 AND  50;

SELECT * FROM campusx.insurance_data
WHERE diabetic = 'Yes' OR smoker = 'Yes';


SELECT distinct region FROM campusx.insurance_data;


SELECT * FROM campusx.insurance_data
WHERE region = 'north';

SELECT * FROM campusx.insurance_data
WHERE region = 'northeast' OR region = 'northwest';

SELECT * FROM campusx.insurance_data
WHERE claim >= 5000;

SELECT * FROM campusx.insurance_data
WHERE age > 50 AND smoker = 'Yes' AND diabetic = 'Yes';

SELECT * FROM campusx.insurance_data
WHERE  smoker = 'No' AND diabetic = 'No' AND bmi < 25;

SELECT * FROM insurance_data
WHERE region IN('northwest','southeast');

SELECT * FROM insurance_data
WHERE smoker != 'Yes';

SELECT * FROM insurance_data
WHERE claim BETWEEN 2000 AND 8000 AND gender = 'female';

SELECT * FROM insurance_data
WHERE gender = 'female' AND region = 'northwest' AND claim BETWEEN 2000 AND 8000;




SELECT * FROM insurance_data
WHERE age > 40 && smoker = 'No'  AND diabetic = 'No' AND CLAIM > 5000;


SELECT * FROM insurance_data;
DELETE FROM insurance_data
WHERE age IS NULL OR age = '';

DELETE FROM insurance_data
WHERE children = 0;


SELECT COUNT(*) FROM insurance_data
WHERE age IS NOT NULL ;

SELECT COUNT(*) FROM insurance_data
WHERE smoker = 'Yes';


SELECT COUNT(*) , region FROM insurance_data
GROUP BY region;

SELECT COUNT(*) FROM insurance_data
WHERE diabetic = 'Yes';

SELECT region,SUM(claim) AS 'total_claim_amount' FROM insurance_data
GROUP BY  region;

SELECT SUM(children) FROM insurance_data;

SELECT COUNT(*) FROM insurance_data
WHERE smoker = 'Yes';

SELECT COUNT(*) , SUM(claim)  FROM insurance_data
WHERE gender = 'female';


SELECT AVG(age) FROM insurance_data;

SELECT AVG(claim) FROM insurance_data;

SELECT gender, AVG(claim) FROM insurance_data
GROUP BY gender;

SELECT smoker, AVG(claim) FROM insurance_data
GROUP BY smoker;

SELECT region,AVG(bmi) FROM insurance_data
GROUP BY region;

SELECT MIN(age) FROM insurance_data;

SELECT MIN(claim) FROM insurance_data;

SELECT region , MIN(claim) FROM insurance_data
GROUP BY region;

SELECT smoker,MIN(bmi) FROM insurance_data
GROUP BY smoker;

SELECT gender,MIN(age) FROM insurance_data
WHERE gender = 'female';

SELECT smoker, MIN(age) FROM insurance_data
WHERE smoker = 'Yes';


SELECT MAX(claim) FROM insurance_data;

SELECT MAX(age) FROM insurance_data;

SELECT region,MAX(claim) FROM insurance_data
GROUP BY region;


SELECT smoker,MAX(bmi) FROM insurance_data
GROUP BY smoker;

SELECT gender,MAX(age) FROM insurance_data
GROUP BY gender;



SELECT region,COUNT(*)  , avg(claim) ,MAX(claim) FROM insurance_data
GROUP BY region;


SELECT avg(claim),MIN(claim) , MAX(claim) FROM insurance_data
WHERE diabetic = 'Yes';

SELECT smoker, avg(claim),Max(claim) FROM insurance_data
GROUP BY smoker
;

SELECT gender,COUNT(*),AVG(age),MAX(claim) FROM insurance_data
GROUP BY gender;

SELECT region,AVG(claim) AS 'avg_claim' FROM insurance_data
GROUP BY region
HAVING AVG(claim) > 5000;

SELECT * FROM insurance_data
ORDER BY claim DESC LIMIT 3;



select * FROM insurance_data;

DELETE FROM insurance_data
WHERE age IS NULL or age = 0;
