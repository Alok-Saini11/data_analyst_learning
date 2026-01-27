use school;
select * from teachers;

-- update
update teachers
set name = 'rahul saini',age = 25
where TeacherID = 5;

-- delete
delete from teachers
where TeacherID = 6;

-- TOP 5 records from table
select * from teachers
limit 5;

-- TOP 5 records from column
select city from teachers
limit 5;

-- Aggregate functions
-- SUM
select sum(Salary) from teachers;

-- Average
select avg(Salary) from teachers;

-- Minimum
select min(Salary) from teachers;

-- Maximum
select max(Salary) from teachers;

-- Count
select count(Salary) from teachers;

