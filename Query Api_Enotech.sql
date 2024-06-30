create database Api_EnoTech

use Api_Enotech

show tables


create table Locations(
/*idLocation int unsigned not null auto_increment primary key,*/
idLocation int auto_increment primary key,
country varchar (50) not null,
url varchar (100) not null
)

select * from Locations

insert into Locations (country,url) values ('España','https://maps.app.goo.gl/5mh1dPim4ENsDuH88'),
('Francia','https://maps.app.goo.gl/tDCMGQ2p6kUVw6om7'),('Italia','https://maps.app.goo.gl/dgRTHRBZLVXCzyoE9'),
('Argentina','https://maps.app.goo.gl/rMXbhdfmtfbYKxoz8'),('Estados Unidos','https://maps.app.goo.gl/EQtB9YVxjggw7UCr5')
,('Gran Bretaña','https://maps.app.goo.gl/vXXNSWarMoPKeaqA6'),('Mexico','https://maps.app.goo.gl/3HwkTvMAhkPi5AQG6'),
('Uruguay','https://maps.app.goo.gl/oqCa5eaoFDEPyPkA9'),('Chile','https://maps.app.goo.gl/XwoFATJR9prLqRdt8')

drop table Locations
drop table wines


create table wines (
idWine int unsigned not null auto_increment primary key ,
winery varchar(50) not null,
wine varchar (50) not null,
id_Location int null,
image varchar (100) null,
FOREIGN KEY (id_Location)
REFERENCES Locations(idLocation))

select * from wines


