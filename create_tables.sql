drop database if exists medical_shop;
create database medical_shop;
use medical_shop;

-- Tables
create table customer (
    customer_id int auto_increment primary key,
    name varchar(100),
    phone varchar(15),
    address text
);

create table medicine (
    medicine_id int auto_increment primary key,
    name varchar(100),
    category varchar(100),
    manufacturer varchar(100),
    price decimal(10, 2),
    expiry_date date,
    quantity_in_stock int check (quantity_in_stock >= 0) -- Assertion to ensure stock cannot be negative
);

create table bill (
    bill_id int auto_increment primary key,
    customer_id int,
    date date,
    total_amount decimal(10, 2),
    foreign key (customer_id) references customer(customer_id)
);

create table bill_items (
    bill_item_id int auto_increment primary key,
    bill_id int,
    medicine_id int,
    quantity int check (quantity > 0), -- Assertion to ensure quantity is always greater than 0
    price decimal(10, 2),
    foreign key (bill_id) references bill(bill_id),
    foreign key (medicine_id) references medicine(medicine_id)
);

-- Views
create view available_medicines as
select * from medicine where expiry_date > curdate() and quantity_in_stock > 0;

create view bill_details as
select b.bill_id, b.date, c.name as customer_name, m.name as medicine_name,
       bi.quantity, bi.price, (bi.quantity * bi.price) as total_price
from bill b
join customer c on b.customer_id = c.customer_id
join bill_items bi on b.bill_id = bi.bill_id
join medicine m on bi.medicine_id = m.medicine_id;

-- Triggers
delimiter $$

create trigger check_expiry_before_billing
before insert on bill_items
for each row
begin
    declare exp date;
    select expiry_date into exp from medicine where medicine_id = new.medicine_id;
    if exp < curdate() then
        signal sqlstate '45000' set message_text = 'cannot bill expired medicine'; -- Trigger checks expiry before billing
    end if;
end$$

create trigger reduce_stock_after_billing
after insert on bill_items
for each row
begin
    update medicine
    set quantity_in_stock = quantity_in_stock - new.quantity
    where medicine_id = new.medicine_id;
end$$

delimiter ;
