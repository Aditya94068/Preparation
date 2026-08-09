CREATE TABLE customers (
	first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone BIGINT ,
    gender VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    pincode INTEGER(255)
);
DROP TABLE customers;
INSERT INTO customers 
(first_name, last_name, email, phone, gender, city, state, pincode)
VALUES 
('Rohan','Sharma','rohan.sharma@gmail.com','9876543211','Male','Mumbai','Maharashtra','400001'),
('Priya','Verma','priya.verma@gmail.com','9876543212','Female','Delhi','Delhi','110001'),
('Amit','Patel','amit.patel@gmail.com','9876543213','Male','Ahmedabad','Gujarat','380001'),
('Sneha','Iyer','sneha.iyer@gmail.com','9876543214','Female','Chennai','Tamil Nadu','600001'),
('Rahul','Singh','rahul.singh@gmail.com','9876543215','Male','Lucknow','Uttar Pradesh','226001'),
('Neha','Gupta','neha.gupta@gmail.com','9876543216','Female','Jaipur','Rajasthan','302001'),
('Vikram','Reddy','vikram.reddy@gmail.com','9876543217','Male','Hyderabad','Telangana','500001'),
('Anjali','Mehta','anjali.mehta@gmail.com','9876543218','Female','Pune','Maharashtra','411001'),
('Karan','Malhotra','karan.malhotra@gmail.com','9876543219','Male','Chandigarh','Punjab','160001'),
('Pooja','Nair','pooja.nair@gmail.com','9876543220','Female','Kochi','Kerala','682001');
