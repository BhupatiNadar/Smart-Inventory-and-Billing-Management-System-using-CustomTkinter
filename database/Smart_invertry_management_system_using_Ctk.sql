create database Smart_invertry_management_system_using_Ctk;

use Smart_invertry_management_system_using_Ctk;

create table UserLogin(
id int auto_increment primary key,
Username varchar(50) NOT NULL UNIQUE,
passward_hash varchar(255) NOT NULL,
role enum("admin","manager","employee") not null default "employee",
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp
);

insert into UserLogin (Username,passward_hash,role)value("Admin","$2b$12$sq6HsD9YsvLiP3n0QoE46OSm77t98n9G3OI/Z.gPD0w49k8veVl6e","admin");

CREATE TABLE category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(30) NOT NULL UNIQUE,
    product_quantity INT NOT NULL CHECK (product_quantity >= 0),
    price DECIMAL(10,2) NOT NULL,
    category_id INT NOT NULL,
    CONSTRAINT fk_product_category
        FOREIGN KEY (category_id)
        REFERENCES category(category_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

INSERT INTO category (category_name) VALUES
('Electronics'),
('Groceries'),
('Stationery'),
('Clothing'),
('Home Appliances');

INSERT INTO product 
(product_name, product_quantity, price, category_id) 
VALUES
('Laptop', 25, 55000.00, 1),
('Smartphone', 40, 18000.00, 1),
('Rice Bag 10kg', 100, 620.50, 2),
('Cooking Oil 1L', 75, 180.00, 2),
('Notebook', 200, 45.00, 3),
('Pen', 500, 10.00, 3),
('T-Shirt', 60, 399.99, 4),
('Jeans', 45, 1299.00, 4),
('Microwave Oven', 10, 8999.00, 5),
('Electric Kettle', 20, 1499.00, 5);

SELECT p.product_id,
       p.product_name,
       c.category_name AS category_name,
       p.product_quantity,
       p.price
FROM product p
JOIN category c
  ON c.category_id = p.category_id
ORDER BY p.product_id ASC
LIMIT 5 OFFSET 0;

CREATE TABLE supplier (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_code VARCHAR(30) NOT NULL UNIQUE,
    supplier_name VARCHAR(50) NOT NULL,
    supplier_contact_no VARCHAR(15),
    supplier_email VARCHAR(100) NOT NULL UNIQUE,
    category_id INT NOT NULL,
    CONSTRAINT fk_supplier_category
        FOREIGN KEY (category_id)
        REFERENCES category(category_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

INSERT INTO supplier 
(supplier_code, supplier_name, supplier_contact_no, supplier_email, category_id)
VALUES
('SUP-ELE-001', 'TechVision Electronics', '9876543210', 'contact@techvision.com', 1),
('SUP-ELE-002', 'Digital World Pvt Ltd', '9123456789', 'sales@digitalworld.com', 1),

('SUP-GRO-001', 'FreshMart Suppliers', '9988776655', 'info@freshmart.com', 2),
('SUP-GRO-002', 'DailyNeeds Wholesale', '9090909090', 'support@dailyneeds.com', 2),

('SUP-STA-001', 'OfficePro Stationers', '8887776665', 'office@officepro.com', 3),
('SUP-STA-002', 'WriteWell Distributors', '7776665554', 'sales@writewell.com', 3),

('SUP-CLO-001', 'FashionHub Traders', '9898989898', 'contact@fashionhub.com', 4),
('SUP-CLO-002', 'UrbanWear Suppliers', '9765432109', 'info@urbanwear.com', 4),

('SUP-HOM-001', 'HomeEase Appliances', '9654321098', 'service@homeease.com', 5),
('SUP-HOM-002', 'ComfortLiving Pvt Ltd', '9543210987', 'support@comfortliving.com', 5);

CREATE TABLE sales (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    invoice_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    total_amount DECIMAL(10,2) NOT NULL CHECK (total_amount >= 0),
    status ENUM ('pending', 'paid', 'prepaid', 'shipped') NOT NULL DEFAULT 'pending'
);

INSERT INTO sales (customer_name, invoice_date, total_amount, status) VALUES
('Ravi Kumar',    '2025-01-10', 12500.00, 'paid'),
('Anita Sharma',  '2025-01-11',  3400.50, 'pending'),
('Suresh Patel',  '2025-01-12',  8900.75, 'prepaid'),
('Neha Verma',    '2025-01-13', 15750.00, 'shipped'),
('Arjun Reddy',   '2025-01-14',  2200.00, 'paid'),
('Priya Nair',    '2025-01-15',  4999.99, 'pending');


