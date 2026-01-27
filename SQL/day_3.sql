use school;

-- Table selection
select * from students;

-- column selection
select city from students;

-- multiple column selection
select city,marks from students;

-- select distinct values
select distinct name from students;

-- count values
select count(distinct name)from students;

-- where
select * from students where city ='delhi';

-- order by
select * from students
order by name asc;

-- AND
select * from students
where name = 'Manish Saini' and city = 'delhi';

-- OR 
select * from students
where name = 'manish Saini' or city = 'delhi';

-- NOT
select * from students
where not city = 'delhi';

-- null values
select city from students
where city is not null;

-- comparison operator
select age from students
where age >= 18;