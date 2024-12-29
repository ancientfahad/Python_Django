-- Active: 1728315354834@@127.0.0.1@3306@POS

CREATE DATABASE POS;

DROP TABLE categories;

CREATE TABLE users (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email_address VARCHAR(50) NOT NULL,
    mobile_number VARCHAR(50) NOT NULL,
    password VARCHAR(500) NOT NULL,
    otp VARCHAR(10) NOT NULL DEFAULT '0',
    create_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
)

--- পাত্রী (FOREIGN KEY) অনন্যা আহমেদের বিয়ে হবে(REFERENCES) ফেনীর(users) ফাহাদ চোধুরীর(PRIMARY KEY) সাথে
--- মরলে দুজন একসাথে মরবা (ON DELETE RESTRICT), বাঁচলে দুজন একসাথে বাঁচবা (ON DELETE CASCADE) (FOREIGN KEY CONSTRAINT)
CREATE TABLE categories (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL, 
    FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    create_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
)

CREATE TABLE products (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price VARCHAR(50) NOT NULL,
    unit VARCHAR(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    category_id BIGINT UNSIGNED NOT NULL, 
    FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`category_id`) REFERENCES categories(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    create_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
)

CREATE TABLE customers (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email_address VARCHAR(50) NOT NULL,
    mobile_number VARCHAR(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    create_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
)

CREATE TABLE customers (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email_address VARCHAR(50) NOT NULL,
    mobile_number VARCHAR(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    create_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
)

CREATE TABLE invoices (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    total VARCHAR(50) NOT NULL,
    discount VARCHAR(50) NOT NULL,
    vat VARCHAR(50) NOT NULL,
    payable VARCHAR(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    customer_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    create_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
)

CREATE TABLE invoice_products (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    quantity VARCHAR(50) NOT NULL,
    sale_price VARCHAR(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    product_id BIGINT UNSIGNED NOT NULL,
    invoice_id BIGINT UNSIGNED NOT NULL,
    customer_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`product_id`) REFERENCES products(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`invoice_id`) REFERENCES invoices(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
    create_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
)

SELECT * FROM users