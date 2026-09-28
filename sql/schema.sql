CREATE DATABASE IF NOT EXISTS querypilot;
USE querypilot;

CREATE TABLE IF NOT EXISTS departments (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  location VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  department_id INT NOT NULL,
  job_title VARCHAR(100) NOT NULL,
  salary DECIMAL(10,2) NOT NULL,
  joining_date DATE NOT NULL,
  FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO departments (name, location) VALUES
('Engineering','Kolkata'),('Data','Bengaluru'),('Human Resources','Delhi'),('Finance','Mumbai');

INSERT INTO employees (name, department_id, job_title, salary, joining_date) VALUES
('Aarav Sen',1,'Software Engineer',72000.00,'2023-06-12'),
('Riya Das',1,'Backend Developer',68000.00,'2024-01-15'),
('Arjun Roy',1,'Software Engineer',76000.00,'2022-08-22'),
('Meera Nair',2,'Data Analyst',62000.00,'2024-07-01'),
('Kabir Shah',2,'Data Engineer',81000.00,'2023-03-18'),
('Ananya Bose',3,'HR Executive',54000.00,'2022-11-07'),
('Vikram Jain',4,'Financial Analyst',65000.00,'2024-02-26');
