use school;
select * from students;

-- LIKE(name starts from character 'A')
select * from students
where city like 'a%';

-- (name ends with character 'A')
select * from students
where city like '%a'

-- ( city which have only four character)
select * from students
where city like '____' ;

-- (city which second character will 'u')
select * from students
where city like '_u%';

-- (check cities which starting character is 'a' and ending charcter will be 'a')
select * from students
where city like '%a' and city like 'a%';

-- IN
select * from students
where city in ('Delhi','Jaipur');

-- Between
select * from students
where age between 18 and 21;

-- (city name between c to i)
select * from students
where city between 'c' and 'i';

-- AS
select Name as full_name from students;

-- JOINS

use school;
create table person(
pid int primary key,
name varchar(50),
address varchar(100)
);
insert into person values
(1,'ram','sikar'),
(2,'shyam','jaipur'),
(3,'ravi','sikar');
select * from person;

Create table orders(
   OID INT PRIMARY KEY,
   orderName varchar(50) not null,
   PID int
   );
INSERT INTO orders (OID, orderName, PID) VALUES
(101, 'Laptop Purchase', 1),
(102, 'Mobile Phone', 2),
(103, 'Book Order', 3),
(104, 'Office Chair', 1),
(105, 'Headphones', 4);

-- Inner join
select * from person
inner join orders
on person.PID = orders.PID;

-- Left join
select * from person
left join orders
on person.PID = orders.PID;

-- Right join
select * from person
right join orders
on person.PID = orders.PID;

-- Self join
select a.Name as c1,b.Name as c2,a.Address
from person a
join person b
where a.Address = b.Address
AND a.PID <> b.PID
LIMIT 0, 1000;





