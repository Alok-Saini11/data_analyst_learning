create database Restaurant;
use Restaurant;

create table person(
pid int primary key,
p_name varchar(50),
address varchar(50)
);
select * from person;

-- Alter
-- 01.Add column
alter table person
add p_lastname varchar(50);

-- 02.Modify
alter table person
modify column address char;

-- 03.Rename
alter table person
rename column p_name to first_name ;

-- 04.drop
alter table person
drop address;

-- Constraints
use restaurant;
create table orders(
o_id int primary key,
o_name varchar(50) not null,
pid int not null unique auto_increment,
age int check(age >= 18),
city varchar(20) default 'sikar',
foreign key(pid) references person(pid));

select * from person;
select * from orders;
