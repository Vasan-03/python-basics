import pyodbc

# #create table:
# db = pyodbc.connect("Driver={SQL Server};""Server=LAPTOP-JS320TV2\SQLEXPRESS;""Database=vasan;""Trusted_Connection=yes;")
# curs = db.cursor()
# curs.execute("create table studentinfo(person varchar(15),age int,city varchar(15))")
# curs.commit()

#insert data:
# x = str(input("enter a name:"))
# y = int(input("enter a age:"))
# z = str(input("enter a city:"))
# val = (x, y, z)
# db = pyodbc.connect("Driver={SQL Server};""Server=LAPTOP-JS320TV2\SQLEXPRESS;""Database=vasan;""Trusted_Connection=yes;")
# curs = db.cursor()
# curs.execute("insert into studentinfo (PERSON,AGE,CITY) values(?,?,?)", val)
# curs.commit()

#fetch data:

# db = pyodbc.connect("Driver={SQL Server};""Server=LAPTOP-JS320TV2\SQLEXPRESS;""Database=vasan;""Trusted_Connection=yes;")
# curs = db.cursor()
# curs.execute("select * from studentinfo")
# res = curs.fetchall()
# for i in res:
#     print(i)

#fetch using where:

# db = pyodbc.connect("Driver={SQL Server};""Server=LAPTOP-JS320TV2\SQLEXPRESS;""Database=vasan;""Trusted_Connection=yes;")
# curs = db.cursor()
# curs.execute("select * from studentinfo where person =?", ("sathish"))
# res = curs.fetchall()
# for i in res:
#     print(i)

#delete row:

# db = pyodbc.connect("Driver={SQL Server};""Server=LAPTOP-JS320TV2\SQLEXPRESS;""Database=vasan;""Trusted_Connection=yes;")
# curs = db.cursor()
# curs.execute("delete from studentinfo where person =?", ("vasan"))
# curs.commit()

#drop table:

# db = pyodbc.connect("Driver={SQL Server};""Server=LAPTOP-JS320TV2\SQLEXPRESS;""Database=vasan;""Trusted_Connection=yes;")
# curs = db.cursor()
# curs.execute("drop table studentinfo")
# curs.commit()

