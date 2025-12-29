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

