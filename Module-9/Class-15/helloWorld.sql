-- Active: 1728315354834@@127.0.0.1@3306@demo
CREATE DATABASE demo;

CREATE TABLE employees (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary BIGINT NOT NULL,
    designation VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    create_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
)

INSERT INTO employees (name, salary, designation, city) VALUES ('Fahad Chowdhury', 102600, 'Technology Support Specialist', 'Dhaka');
INSERT INTO employees (name, salary, designation, city) VALUES ('Anannya Chowdhury', 200000, 'Technology Support Manager', 'Dhaka');
INSERT INTO employees (name, salary, designation, city) VALUES ('X', 0, 'X', 'X');

SELECT * FROM employees;

SELECT id, salary FROM employees;

SELECT * FROM employees WHERE salary > 100000 AND salary < 150000;

SELECT id, name FROM employees WHERE salary > 100000 AND salary < 150000;

UPDATE employees SET salary = 120000 WHERE id = 1;

