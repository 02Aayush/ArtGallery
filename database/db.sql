create database artdb;
use artdb;

create table loginmaster (
userid varchar(30) primary key,
pwd varchar(10),
userrole enum ('admin','artist')
);

insert into loginmaster values('admin@art','super','admin');

create table catagories(
cid integer primary key auto_increment,
catagory varchar(30)
);

insert into catagories(catagory) values('Oil');
insert into catagories(catagory) values('ACRYLIC');
insert into catagories(catagory) values('WATERCOLOR');
insert into catagories(catagory) values('GOUACHE');
insert into catagories(catagory) values('PASTEL');
insert into catagories(catagory) values('ENCAUSTIC');
insert into catagories(catagory) values('FRESCO');
insert into catagories(catagory) values('SPRAY PAINT');
insert into catagories(catagory) values('TEMPERA');
insert into catagories(catagory) values('ENAMEL');
insert into catagories(catagory) values('Bhil');
insert into catagories(catagory) values('Warli');
insert into catagories(catagory) values('Gond');
insert into catagories(catagory) values('Santhal');
insert into catagories(catagory) values('Saora');
insert into catagories(catagory) values('Kurumba');
insert into catagories(catagory) values('Madhubani');


create table paintings(
pid integer primary key auto_increment,
artist varchar(20),
cid integer,
size varchar(20),
price integer,
available enum('y','n') default 'y',
owner varchar(30)
);


create table members
(
emailid varchar(30) primary  key,
name varchar(30),
contactno varchar(10),
joindate DATETIME DEFAULT CURRENT_TIMESTAMP,
membershiptype enum('regular','premium'),
uptodate date
);