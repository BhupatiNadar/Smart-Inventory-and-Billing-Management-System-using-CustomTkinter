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

ALTER TABLE product
ADD COLUMN reorder_level INT NOT NULL DEFAULT 10
CHECK (reorder_level >= 0);

select * from product;


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


UPDATE product
SET reorder_level = CASE product_name
    WHEN 'Laptop' THEN 10
    WHEN 'Smartphone' THEN 15
    WHEN 'Rice Bag 10kg' THEN 30
    WHEN 'Cooking Oil 1L' THEN 25
    WHEN 'Notebook' THEN 50
    WHEN 'Pen' THEN 100
    WHEN 'T-Shirt' THEN 20
    WHEN 'Jeans' THEN 15
    WHEN 'Microwave Oven' THEN 5
    WHEN 'Electric Kettle' THEN 8
END;

CREATE TABLE sales_items (
    sales_item_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_sales_items_sales
        FOREIGN KEY (invoice_id)
        REFERENCES sales(invoice_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_sales_items_product
        FOREIGN KEY (product_id)
        REFERENCES product(product_id)
        ON DELETE RESTRICT
);

INSERT INTO sales_items (invoice_id, product_id, quantity, unit_price) VALUES
-- Invoice 1: Ravi Kumar
(1, 1, 1, 55000.00),   -- Laptop
(1, 5, 5, 45.00),     -- Notebook

-- Invoice 2: Anita Sharma
(2, 6, 10, 10.00),    -- Pen
(2, 4, 3, 180.00),    -- Cooking Oil 1L

-- Invoice 3: Suresh Patel
(3, 2, 1, 18000.00),  -- Smartphone
(3, 10, 2, 1499.00), -- Electric Kettle

-- Invoice 4: Neha Verma
(4, 1, 1, 55000.00),  -- Laptop
(4, 8, 2, 1299.00),  -- Jeans

-- Invoice 5: Arjun Reddy
(5, 6, 20, 10.00),   -- Pen

-- Invoice 6: Priya Nair
(6, 9, 1, 8999.00);  -- Microwave Oven

UPDATE sales s
SET total_amount = (
    SELECT SUM(quantity * unit_price)
    FROM sales_items si
    WHERE si.invoice_id = s.invoice_id
);
