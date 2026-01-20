use school;
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    Course VARCHAR(30),
    City VARCHAR(30),
    Marks INT
);
INSERT INTO Students VALUES
(1,'Amit Sharma','Male',20,'BCA','Delhi',78),
(2,'Neha Verma','Female',19,'BCA','Jaipur',85),
(3,'Rahul Meena','Male',21,'BSc','Kota',72),
(4,'Pooja Singh','Female',20,'BCom','Delhi',88),
(5,'Vikas Kumar','Male',22,'BA','Patna',65),
(6,'Anjali Gupta','Female',21,'BCA','Agra',91),
(7,'Rohit Yadav','Male',20,'BSc','Gurgaon',70),
(8,'Sneha Patel','Female',19,'BCA','Ahmedabad',84),
(9,'Arjun Rathore','Male',23,'BCom','Indore',68),
(10,'Kavita Joshi','Female',21,'BA','Udaipur',73),

(11,'Suresh Rao','Male',22,'BSc','Bhopal',77),
(12,'Nidhi Jain','Female',20,'BCA','Ajmer',89),
(13,'Manish Saini','Male',21,'BA','Alwar',66),
(14,'Priya Mishra','Female',22,'BCom','Lucknow',92),
(15,'Deepak Choudhary','Male',20,'BCA','Sikar',74),
(16,'Ritu Khandelwal','Female',19,'BSc','Jaipur',81),
(17,'Kunal Verma','Male',23,'BA','Delhi',69),
(18,'Simran Kaur','Female',21,'BCA','Chandigarh',87),
(19,'Ajay Singh','Male',22,'BCom','Kanpur',71),
(20,'Meena Solanki','Female',20,'BA','Jodhpur',75),

(21,'Harsh Malhotra','Male',21,'BCA','Delhi',90),
(22,'Ayesha Khan','Female',22,'BSc','Bhopal',83),
(23,'Nitin Agarwal','Male',19,'BCA','Mathura',79),
(24,'Rakhi Pandey','Female',20,'BA','Varanasi',68),
(25,'Sanjay Patel','Male',23,'BCom','Surat',72),
(26,'Komal Arora','Female',21,'BCA','Panipat',86),
(27,'Rakesh Thakur','Male',22,'BA','Shimla',64),
(28,'Isha Saxena','Female',20,'BSc','Bareilly',88),
(29,'Vivek Tiwari','Male',21,'BCA','Rewa',76),
(30,'Naina Kapoor','Female',19,'BCom','Noida',82),

(31,'Prakash Jha','Male',22,'BA','Darbhanga',67),
(32,'Shalini Roy','Female',21,'BCA','Kolkata',91),
(33,'Mohit Bansal','Male',20,'BSc','Hisar',74),
(34,'Payal Goyal','Female',22,'BCom','Sirsa',85),
(35,'Sunil Pawar','Male',23,'BA','Nagpur',63),
(36,'Divya Nair','Female',21,'BCA','Kochi',89),
(37,'Aman Arvind','Male',19,'BSc','Chennai',78),
(38,'Riya Bose','Female',20,'BA','Kolkata',80),
(39,'Lokesh Prajapat','Male',22,'BCA','Tonk',71),
(40,'Shweta Kulkarni','Female',23,'BCom','Pune',84),

(41,'Ankit Raj','Male',21,'BA','Ranchi',69),
(42,'Farah Ali','Female',20,'BCA','Hyderabad',92),
(43,'Pankaj Yogi','Male',22,'BSc','Bundi',73),
(44,'Monika Chauhan','Female',19,'BA','Meerut',77),
(45,'Gaurav Saxena','Male',23,'BCom','Moradabad',66),
(46,'Preeti Kumari','Female',21,'BCA','Gaya',88),
(47,'Shubham Mishra','Male',20,'BSc','Satna',75),
(48,'Rashmi Shetty','Female',22,'BA','Mangalore',83),
(49,'Naveen Soni','Male',21,'BCA','Bikaner',79),
(50,'Aarti Malviya','Female',20,'BCom','Ujjain',86);
select*from students;

CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    Subject VARCHAR(30),
    Experience INT,
    City VARCHAR(30),
    Salary INT
);

INSERT INTO Teachers VALUES
(1,'Rakesh Sharma','Male',45,'DBMS',18,'Delhi',65000),
(2,'Sunita Verma','Female',38,'Computer Networks',12,'Jaipur',58000),
(3,'Anil Mehta','Male',50,'Operating System',25,'Mumbai',72000),
(4,'Pooja Singh','Female',35,'Data Structures',10,'Lucknow',54000),
(5,'Rajesh Kumar','Male',42,'Java Programming',15,'Patna',60000),

(6,'Neelam Gupta','Female',40,'Python',14,'Agra',62000),
(7,'Vikas Chauhan','Male',48,'Software Engineering',20,'Noida',70000),
(8,'Kiran Patel','Female',37,'Web Development',11,'Ahmedabad',56000),
(9,'Sanjay Mishra','Male',55,'Computer Architecture',30,'Kanpur',80000),
(10,'Meena Joshi','Female',33,'C Programming',8,'Udaipur',52000),

(11,'Amit Tiwari','Male',41,'Machine Learning',13,'Bhopal',68000),
(12,'Ritu Malhotra','Female',39,'Artificial Intelligence',12,'Chandigarh',69000),
(13,'Prakash Rao','Male',52,'Data Mining',27,'Hyderabad',75000),
(14,'Sneha Kulkarni','Female',36,'Cloud Computing',9,'Pune',61000),
(15,'Arun Saxena','Male',47,'Cyber Security',19,'Meerut',72000),

(16,'Nisha Kapoor','Female',34,'DBMS',7,'Noida',55000),
(17,'Deepak Yadav','Male',44,'Linux Administration',16,'Gurgaon',67000),
(18,'Rashmi Nair','Female',42,'Big Data',15,'Kochi',73000),
(19,'Mahesh Solanki','Male',49,'IoT',22,'Indore',71000),
(20,'Farzana Khan','Female',31,'HTML & CSS',6,'Aligarh',48000);
select*from teachers ;
