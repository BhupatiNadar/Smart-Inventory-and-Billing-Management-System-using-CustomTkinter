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


