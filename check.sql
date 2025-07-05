CREATE DATABASE sms2;

USE sms2;

CREATE TABLE student (
  roll_no VARCHAR(20) PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  gender VARCHAR(10),
  contact VARCHAR(15),
  dob VARCHAR(20),
  address TEXT
);

mysql -u root -p
